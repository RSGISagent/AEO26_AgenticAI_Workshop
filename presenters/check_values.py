"""Reference numbers for the AEO26 practical (the answer key behind CHECK_VALUES.md).

Participants' agents build ``outputs/severity_summary.csv`` (WORKBOOK Step 6). In Step 7
participants compare it with these values: the "Did you get 52 %? If not, why not?" moment.
The script is deliberately plain and independent of any agent's code.

For each NSW FESM 2019/20 severity class it reports the area (ha, from 10 m EPSG:3577 pixels
of 0.01 ha), the share of the study area, the mean NDVI in autumn 2019, 2020 and 2025, and the
number of greater glider records inside the class (2000-2019, 2020 onwards, and all years).
A second table puts the 2000-2019 records per 1,000 ha of tree cover (ESA WorldCover 2020),
with the records per year, for the "what do the glider counts mean?" discussion.

Usage
-----
python presenters/check_values.py            # print the Markdown tables
python presenters/check_values.py --out table.md
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import rasterio
from rasterio.transform import rowcol
from rasterio.warp import transform as warp_transform

DATA = Path(__file__).resolve().parents[1] / "data"
YEARS = (2019, 2020, 2025)
S2_NODATA = -999
FESM_NODATA = 255
PIXEL_HA = 0.01  # a 10 m x 10 m pixel
TREE_COVER = 10  # ESA WorldCover 2020 class code for tree cover
CLASSES: dict[int, str] = {0: "unburnt / outside", 2: "low", 3: "moderate", 4: "high", 5: "extreme"}


@dataclass(frozen=True)
class ClassSummary:
    """Reference values for one fire-severity class."""

    code: int
    name: str
    area_ha: float
    share_pct: float
    mean_ndvi: Mapping[int, float]
    gliders_2000_2019: int
    gliders_2020_on: int
    gliders_all: int


@dataclass(frozen=True)
class ForestDensity:
    """Greater glider records from 2000-2019 per area of forest in one fire-severity class."""

    name: str
    area_ha: float
    tree_pct: float
    gliders_on_trees: int
    per_1000_ha_trees: float


def read_ndvi(path: Path) -> np.ndarray:
    """Return NDVI (float64, NaN where nodata or NIR + red is zero) from a 3-band composite."""
    with rasterio.open(path) as ds:
        red, nir = ds.read(1).astype(np.float64), ds.read(2).astype(np.float64)
        nodata = (ds.read(1) == S2_NODATA) | (ds.read(2) == S2_NODATA)
    denom = nir + red
    with np.errstate(divide="ignore", invalid="ignore"):
        ndvi = (nir - red) / denom
    return np.where(nodata | (denom == 0), np.nan, ndvi)


def glider_pixels(records: Path, transform: rasterio.Affine, shape: tuple[int, int]) -> np.ndarray:
    """Return an (n, 3) int array of (row, col, year) for records that fall on the grid."""
    with records.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    lon = [float(r["longitude"]) for r in rows]
    lat = [float(r["latitude"]) for r in rows]
    xs, ys = warp_transform("EPSG:4326", "EPSG:3577", lon, lat)
    r, c = rowcol(transform, xs, ys)
    out = np.column_stack([np.asarray(r), np.asarray(c), [int(row["year"]) for row in rows]])
    on_grid = (out[:, 0] >= 0) & (out[:, 0] < shape[0]) & (out[:, 1] >= 0) & (out[:, 1] < shape[1])
    return out[on_grid]


def summarise(data: Path = DATA) -> tuple[list[ClassSummary], dict[str, int]]:
    """Compute the per-class reference values and a few totals."""
    with rasterio.open(data / "fire_severity_2019_20.tif") as ds:
        fesm, transform, shape = ds.read(1), ds.transform, ds.shape
    ndvi = {year: read_ndvi(data / f"sentinel2_{year}.tif") for year in YEARS}
    pix = glider_pixels(data / "glider_records.csv", transform, shape)
    glider_class = fesm[pix[:, 0], pix[:, 1]]
    years = pix[:, 2]
    valid = fesm != FESM_NODATA
    n_valid = int(valid.sum())

    def summary(code: int, name: str) -> ClassSummary:
        mask = fesm == code
        here = glider_class == code
        return ClassSummary(
            code=code,
            name=name,
            area_ha=float(mask.sum()) * PIXEL_HA,
            share_pct=100.0 * float(mask.sum()) / n_valid,
            mean_ndvi={y: float(np.nanmean(ndvi[y][mask])) for y in YEARS},
            gliders_2000_2019=int((here & (years >= 2000) & (years <= 2019)).sum()),
            gliders_2020_on=int((here & (years >= 2020)).sum()),
            gliders_all=int(here.sum()),
        )

    totals = {
        "pixels_with_severity": n_valid,
        "pixels_nodata_severity": int((~valid).sum()),
        "gliders_in_file": sum(1 for _ in (data / "glider_records.csv").open(encoding="utf-8")) - 1,
        "gliders_on_grid": len(pix),
        "gliders_2000_2019_on_grid": int(((years >= 2000) & (years <= 2019)).sum()),
        **{f"s2_nodata_pixels_{y}": int(np.isnan(ndvi[y]).sum()) for y in YEARS},
    }
    return [summary(code, name) for code, name in CLASSES.items()], totals


def forest_density(data: Path = DATA) -> tuple[list[ForestDensity], dict[int, int]]:
    """Glider records 2000-2019 per 1,000 ha of tree cover in each class, and records per year.

    Raw counts mix three things: how big each class is, how much of it is forest, and where people
    looked. Dividing by the area of tree cover removes the first two; the records per year show the
    third (survey effort jumped after the fire).
    """
    with rasterio.open(data / "fire_severity_2019_20.tif") as ds:
        fesm, transform, shape = ds.read(1), ds.transform, ds.shape
    with rasterio.open(data / "land_cover_2020.tif") as ds:
        tree = ds.read(1) == TREE_COVER
    pix = glider_pixels(data / "glider_records.csv", transform, shape)
    rows, cols, years = pix[:, 0], pix[:, 1], pix[:, 2]
    pre_fire_on_trees = tree[rows, cols] & (years >= 2000) & (years <= 2019)
    glider_class = fesm[rows, cols]

    densities = []
    for code, name in CLASSES.items():
        in_class = fesm == code
        area_ha = float(in_class.sum()) * PIXEL_HA
        tree_ha = float((in_class & tree).sum()) * PIXEL_HA
        n = int((pre_fire_on_trees & (glider_class == code)).sum())
        densities.append(ForestDensity(name, area_ha, 100.0 * tree_ha / area_ha, n, 1000.0 * n / tree_ha))
    per_year = {year: int((years == year).sum()) for year in range(2017, int(years.max()) + 1)}
    return densities, per_year


def density_markdown(densities: Sequence[ForestDensity], per_year: Mapping[int, int]) -> str:
    """Format the forest-density table and the records per year as Markdown."""
    header = (
        "| Severity | Area (ha) | Tree cover | Glider records 2000-2019 on tree cover "
        "| Per 1,000 ha of tree cover |\n|---|---:|---:|---:|---:|\n"
    )
    body = "".join(
        f"| {d.name} | {d.area_ha:,.0f} | {d.tree_pct:.0f} % | {d.gliders_on_trees} "
        f"| {d.per_1000_ha_trees:.1f} |\n"
        for d in densities
    )
    years = ", ".join(f"{year}: {n}" for year, n in per_year.items())
    return header + body + f"\n- Glider records per year: {years}.\n"


def to_markdown(classes: Sequence[ClassSummary], totals: Mapping[str, int]) -> str:
    """Format the reference values as a Markdown table plus totals."""
    burnt = [c for c in classes if c.code != 0]
    header = (
        "| Severity (FESM code) | Area (ha) | Share of study area | Mean NDVI 2019 | 2020 | 2025 "
        "| Glider records 2000-2019 | 2020 on | All years |\n"
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|\n"
    )
    body = "".join(
        f"| {c.name} ({c.code}) | {c.area_ha:,.0f} | {c.share_pct:.1f} % | "
        + " | ".join(f"{c.mean_ndvi[y]:.2f}" for y in YEARS)
        + f" | {c.gliders_2000_2019} | {c.gliders_2020_on} | {c.gliders_all} |\n"
        for c in classes
    )
    total_ha = sum(c.area_ha for c in classes)
    burnt_ha = sum(c.area_ha for c in burnt)
    lines = [
        f"- Study area with a severity value: {total_ha:,.0f} ha; burnt (low to extreme): "
        f"{burnt_ha:,.0f} ha ({100 * burnt_ha / total_ha:.1f} %).",
        f"- Severity nodata pixels (code 255): {totals['pixels_nodata_severity']:,}.",
        f"- Glider records in the file: {totals['gliders_in_file']}; on the raster grid: "
        f"{totals['gliders_on_grid']}; of those from 2000-2019: {totals['gliders_2000_2019_on_grid']}.",
        "- Sentinel-2 nodata pixels (excluded from the NDVI means): "
        + ", ".join(f"{y}: {totals[f's2_nodata_pixels_{y}']:,}" for y in YEARS)
        + ".",
    ]
    return header + body + "\n" + "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    """Command-line entry point."""
    parser = argparse.ArgumentParser(description="Print the practical's reference values.")
    parser.add_argument("--data", type=Path, default=DATA, help="data folder")
    parser.add_argument("--out", type=Path, help="also write the Markdown table here")
    args = parser.parse_args(argv)
    text = to_markdown(*summarise(args.data))
    text += "\nGlider records per area of forest (CHECK_VALUES.md, second discussion):\n\n"
    text += density_markdown(*forest_density(args.data))
    print(text, end="")
    if args.out:
        args.out.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
