"""Make the example figures shown in WORKBOOK.md: the "answers" for Steps 3 and 6.

Writes three PNGs to ``examples/`` from the files in ``data/``:

- ``before_after.png``: false colour (SWIR1, NIR, red) for autumn 2019, 2020 and 2025 with one
  shared stretch, and the 2000-2019 greater glider records on the 2019 panel (Steps 2-4).
- ``ndvi_change.png``: NDVI change 2019 -> 2020 and 2020 -> 2025 on one diverging scale (Step 6).
- ``fire_severity_and_gliders.png``: a still picture of what ``glider_map.html`` shows (Step 6).

Usage
-----
python presenters/make_examples.py
"""

from __future__ import annotations

import csv
import io
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import rasterio  # noqa: E402
from matplotlib import patheffects  # noqa: E402
from matplotlib.colors import BoundaryNorm, ListedColormap  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402
from PIL import Image  # noqa: E402
from rasterio.warp import transform as warp_transform  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DATA, OUT = ROOT / "data", ROOT / "examples"
YEARS = (2019, 2020, 2025)
S2_NODATA, SCALE = -999, 10_000
STEP = 2  # plot every 2nd pixel (20 m), which is plenty for these figure sizes
PIXEL_M = 10 * STEP
DPI = 100

# Okabe-Ito colour-blind-safe colours
SKY_BLUE, BLUISH_GREEN, YELLOW, ORANGE, VERMILLION, BLACK = (
    "#56B4E9",
    "#009E73",
    "#F0E442",
    "#E69F00",
    "#D55E00",
    "#000000",
)
SEVERITY = {  # FESM code: (label, colour)
    0: ("Unburnt, or outside the fire", "#DDDDDD"),
    2: ("Low", YELLOW),
    3: ("Moderate", ORANGE),
    4: ("High", VERMILLION),
    5: ("Extreme", BLACK),
}
S2_SOURCE = "Sentinel-2 autumn (Mar–May) median composites: Digital Earth Australia, CC BY 4.0."
ALA_SOURCE = "Greater glider records: Atlas of Living Australia."
FESM_SOURCE = "Fire severity: NSW FESM 2019/20, DCCEEW, CC BY."


def read_s2(year: int) -> np.ndarray:
    """Return (red, nir, swir1) reflectance as a (3, rows, cols) array, NaN where there's no data."""
    with rasterio.open(DATA / f"sentinel2_{year}.tif") as ds:
        dn = ds.read()[:, ::STEP, ::STEP].astype(np.float32)
    return np.where(dn == S2_NODATA, np.nan, dn / SCALE)


def ndvi(refl: np.ndarray) -> np.ndarray:
    """NDVI = (NIR - red) / (NIR + red)."""
    red, nir = refl[0], refl[1]
    return (nir - red) / (nir + red)


def glider_pixels() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return the glider records as (column, row) on the plotted grid, plus their years."""
    with (DATA / "glider_records.csv").open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    lon = [float(r["longitude"]) for r in rows]
    lat = [float(r["latitude"]) for r in rows]
    xs, ys = warp_transform("EPSG:4326", "EPSG:3577", lon, lat)  # degrees -> metres on the grid
    with rasterio.open(DATA / "fire_severity_2019_20.tif") as ds:
        cols, rws = ~ds.transform * (np.asarray(xs), np.asarray(ys))
    years = np.array([int(r["year"]) for r in rows])
    return np.asarray(cols) / STEP, np.asarray(rws) / STEP, years


def add_scale_bar(ax: plt.Axes, n_rows: int, km: int = 5) -> None:
    """Draw a 5 km scale bar, readable on any background, in the lower-left corner."""
    length = km * 1000 / PIXEL_M
    x0, y0 = 0.05 * n_rows, 0.93 * n_rows
    ax.plot([x0, x0 + length], [y0, y0], color="white", lw=6, solid_capstyle="butt")
    ax.plot([x0, x0 + length], [y0, y0], color="black", lw=2.5, solid_capstyle="butt")
    ax.text(
        x0 + length / 2,
        y0 - 0.035 * n_rows,
        f"{km} km",
        color="black",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold",
        bbox={"boxstyle": "round,pad=0.2", "facecolor": "white", "alpha": 0.8, "lw": 0},
    )


def true_north_angle() -> float:
    """Degrees clockwise from the top of the map to true north, at the study-area centre.

    The rasters use GDA94 / Australian Albers (EPSG:3577), so true north is only straight up
    along 132 deg E. Here it's about 8 deg clockwise of straight up.
    """
    with rasterio.open(DATA / "fire_severity_2019_20.tif") as ds:
        left, bottom, right, top = ds.bounds
        crs = ds.crs
    lon, lat = warp_transform(crs, "EPSG:4326", [(left + right) / 2], [(bottom + top) / 2])
    xs, ys = warp_transform("EPSG:4326", crs, [lon[0], lon[0]], [lat[0], lat[0] + 0.01])
    return float(np.degrees(np.arctan2(xs[1] - xs[0], ys[1] - ys[0])))


def add_north_arrow(ax: plt.Axes, n_rows: int, angle: float) -> None:
    """Draw a north arrow pointing to true north in the lower-right corner of a panel."""
    length = 0.09 * n_rows
    x0, y0 = 0.93 * n_rows, 0.95 * n_rows  # tail of the arrow (image rows grow downwards)
    dx, dy = length * np.sin(np.radians(angle)), -length * np.cos(np.radians(angle))
    ax.annotate(
        "",
        xy=(x0 + dx, y0 + dy),
        xytext=(x0, y0),
        arrowprops={
            "arrowstyle": "-|>,head_width=0.45,head_length=0.9",
            "color": "black",
            "lw": 2.5,
            "path_effects": [patheffects.withStroke(linewidth=5, foreground="white")],
        },
    )
    ax.text(
        x0 + 1.25 * dx,
        y0 + 1.25 * dy,
        "N",
        color="black",
        ha="center",
        va="bottom",
        fontsize=11,
        fontweight="bold",
        bbox={"boxstyle": "round,pad=0.2", "facecolor": "white", "alpha": 0.8, "lw": 0},
    )


def caption(fig: plt.Figure, text: str) -> None:
    """Put a one-line source caption under the figure."""
    fig.text(0.5, 0.01, text, ha="center", va="bottom", fontsize=9, color="#444444", wrap=True)


def before_after(refl: dict[int, np.ndarray], gliders: tuple[np.ndarray, ...], north: float) -> Path:
    """Three false-colour panels with one shared 2-98 % stretch per band."""
    rgb = {y: np.stack([r[2], r[1], r[0]], axis=-1) for y, r in refl.items()}  # SWIR1, NIR, red
    stacked = np.concatenate([v.reshape(-1, 3) for v in rgb.values()])
    lo, hi = np.nanpercentile(stacked, 2, axis=0), np.nanpercentile(stacked, 98, axis=0)
    titles = {
        2019: "Autumn 2019: before the fire",
        2020: "Autumn 2020: after the fire",
        2025: "Autumn 2025: five years on",
    }
    fig, axes = plt.subplots(1, 3, figsize=(15, 5.7), dpi=DPI)
    for ax, (year, img) in zip(axes, rgb.items(), strict=True):
        ax.imshow(np.nan_to_num(np.clip((img - lo) / (hi - lo), 0, 1)), interpolation="antialiased")
        ax.set_title(titles[year], fontsize=13)
        ax.set_axis_off()
    cols, rws, years = gliders
    pre = (years >= 2000) & (years <= 2019)
    axes[0].scatter(
        cols[pre],
        rws[pre],
        s=9,
        c="white",
        edgecolors="black",
        linewidths=0.4,
        label="Greater glider records, 2000–2019",
    )
    axes[0].legend(loc="upper right", fontsize=9, framealpha=0.85)
    add_scale_bar(axes[0], refl[2019].shape[1])
    add_north_arrow(axes[0], refl[2019].shape[1], north)
    fig.suptitle(
        "Tallaganda study area, NSW · false colour: SWIR1 (red), NIR (green), red (blue)"
        " · burnt forest shows as dark magenta",
        fontsize=11,
        y=0.97,
    )
    caption(fig, f"{S2_SOURCE} {ALA_SOURCE} One colour stretch for all three years.")
    fig.subplots_adjust(left=0.01, right=0.99, top=0.88, bottom=0.07, wspace=0.03)
    return save(fig, "before_after.png")


def ndvi_change(refl: dict[int, np.ndarray], north: float) -> Path:
    """Two NDVI-change panels on one diverging scale centred on zero."""
    v = {y: ndvi(r) for y, r in refl.items()}
    panels = {"2019 → 2020: the fire": v[2020] - v[2019], "2020 → 2025: recovery": v[2025] - v[2020]}
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 6.6), dpi=DPI)
    im = None
    for ax, (title, change) in zip(axes, panels.items(), strict=True):
        im = ax.imshow(change, cmap="BrBG", vmin=-0.6, vmax=0.6, interpolation="antialiased")
        ax.set_title(title, fontsize=13)
        ax.set_axis_off()
    add_scale_bar(axes[0], v[2019].shape[1])
    add_north_arrow(axes[0], v[2019].shape[1], north)
    cbar = fig.colorbar(im, ax=axes, orientation="horizontal", fraction=0.05, pad=0.03, aspect=45)
    cbar.set_label("Change in NDVI (no units): brown = less green, green = greener", fontsize=11)
    fig.suptitle("Tallaganda study area, NSW · change in greenness (NDVI)", fontsize=12, y=0.98)
    caption(fig, S2_SOURCE)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.24, wspace=0.03)
    return save(fig, "ndvi_change.png")


def severity_map(gliders: tuple[np.ndarray, ...], north: float) -> Path:
    """Fire-severity classes with the glider records on top: a still view of glider_map.html."""
    with rasterio.open(DATA / "fire_severity_2019_20.tif") as ds:
        fesm = ds.read(1)[::STEP, ::STEP]
    codes = list(SEVERITY)
    index = np.full(fesm.shape, np.nan)
    for i, code in enumerate(codes):
        index[fesm == code] = i
    cmap = ListedColormap([colour for _, colour in SEVERITY.values()])
    norm = BoundaryNorm(np.arange(-0.5, len(codes)), cmap.N)
    fig, ax = plt.subplots(figsize=(10, 7.3), dpi=DPI)
    ax.imshow(index, cmap=cmap, norm=norm, interpolation="nearest")
    cols, rws, years = gliders
    pre, post = (years >= 2000) & (years <= 2019), years >= 2020
    ax.scatter(cols[pre], rws[pre], s=16, c=SKY_BLUE, edgecolors="black", linewidths=0.5)
    ax.scatter(cols[post], rws[post], s=20, marker="^", c=BLUISH_GREEN, edgecolors="black", linewidths=0.5)
    ax.set_axis_off()
    add_scale_bar(ax, fesm.shape[1])
    add_north_arrow(ax, fesm.shape[1], north)
    handles = [Patch(facecolor=c, edgecolor="#888888", label=lab) for lab, c in SEVERITY.values()]
    handles += [
        Line2D(
            [],
            [],
            marker="o",
            ls="",
            markerfacecolor=SKY_BLUE,
            markeredgecolor="black",
            label="Glider records, 2000–2019",
        ),
        Line2D(
            [],
            [],
            marker="^",
            ls="",
            markerfacecolor=BLUISH_GREEN,
            markeredgecolor="black",
            label="Glider records, 2020 on",
        ),
    ]
    ax.legend(
        handles=handles,
        loc="upper left",
        bbox_to_anchor=(1.01, 1),
        fontsize=10,
        title="Fire severity, 2019–20",
        title_fontsize=11,
        frameon=False,
    )
    ax.set_title("Tallaganda study area, NSW · fire severity and greater glider records", fontsize=12)
    caption(fig, f"{FESM_SOURCE} {ALA_SOURCE}")
    fig.subplots_adjust(left=0.01, right=0.70, top=0.93, bottom=0.06)
    return save(fig, "fire_severity_and_gliders.png")


def save(fig: plt.Figure, name: str) -> Path:
    """Save a figure to examples/ as a compact 256-colour PNG, and close it."""
    OUT.mkdir(exist_ok=True)
    path = OUT / name
    buffer = io.BytesIO()
    fig.savefig(buffer, dpi=DPI, format="png")
    plt.close(fig)
    buffer.seek(0)
    # 256 colours is plenty for these figures and makes the files several times smaller
    Image.open(buffer).convert("RGB").quantize(colors=256, method=Image.Quantize.MEDIANCUT).save(
        path, optimize=True
    )
    return path


def main() -> None:
    """Build all three example figures and print a few sanity numbers."""
    refl = {y: read_s2(y) for y in YEARS}
    for y, r in refl.items():
        print(f"{y}: reflectance {np.nanmin(r):.3f} to {np.nanmax(r):.3f}")
    gliders = glider_pixels()
    print(
        f"glider records: {len(gliders[2])}, of which 2000–2019: "
        f"{int(((gliders[2] >= 2000) & (gliders[2] <= 2019)).sum())}"
    )
    north = true_north_angle()
    print(f"true north: {north:.1f} degrees clockwise of straight up")
    for path in (before_after(refl, gliders, north), ndvi_change(refl, north), severity_map(gliders, north)):
        print(f"wrote {path.relative_to(ROOT)} ({path.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
