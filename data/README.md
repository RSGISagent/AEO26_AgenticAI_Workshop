# data/: what each file is

Inputs for the Tallaganda study area: a 20 × 20 km square west of Braidwood, NSW, burnt in the
2019–20 Black Summer fires. **Read-only: don't change these files.** Licences and the attribution to
keep with any figure you share are in [`ATTRIBUTION.md`](ATTRIBUTION.md). File sizes and SHA-256
hashes are in [`MANIFEST.csv`](MANIFEST.csv). Where each file came from (satellite image lists,
queries and access dates) is in [`provenance/`](provenance/).

## Files

| File | What it shows | Values |
|---|---|---|
| `sentinel2_2019.tif` | Sentinel-2 surface reflectance, autumn (1 March to 31 May) 2019: **before** the fire | 3 bands, see below |
| `sentinel2_2020.tif` | The same for autumn 2020: two to four months **after** the fire | 3 bands |
| `sentinel2_2025.tif` | The same for autumn 2025: **five years on** | 3 bands |
| `fire_severity_2019_20.tif` | NSW Fire Extent and Severity Mapping (FESM) 2019/20 | classes, see below |
| `land_cover_2020.tif` | ESA WorldCover 2020 land cover (for example, tree cover vs grassland) | classes, see below |
| `glider_records.csv` | 551 greater glider (*Petauroides volans*) records from the Atlas of Living Australia inside the study area | one row per record |
| `study_area.geojson` | The study-area outline | longitude/latitude (WGS84) |

## The rasters

- All five rasters share one grid: **EPSG:3577** (GDA94 / Australian Albers, an equal-area projection
  in metres), **10 m pixels**, 2000 × 2000 pixels. They line up pixel for pixel, so no resampling is
  needed. One pixel is 100 m² = **0.01 ha**.
- **Sentinel-2 bands, in order:** 1 = red (B04), 2 = near infrared, NIR (B08), 3 = short-wave
  infrared, SWIR1 (B11, about 1610 nm; 20 m native, resampled to 10 m).
- **Sentinel-2 values** are whole numbers: reflectance × 10,000. Divide by 10,000 to get reflectance
  (0–1). **Nodata = −999** (no clear observation); mask it before any calculation.
- Each Sentinel-2 file is a per-pixel median of the cloud-free autumn images from Digital Earth
  Australia's Sentinel-2 Analysis Ready Data (NBART surface reflectance).
- Useful indices: NDVI = (NIR − red) / (NIR + red), greenness. NDMI = (NIR − SWIR1) / (NIR + SWIR1),
  canopy moisture. Both run from −1 to 1, and both drop sharply where a fire burnt the canopy.
- A false-colour view that shows fire scars well: red = SWIR1, green = NIR, blue = red. Use the same
  colour stretch for every year if you want to compare years.
- **Fire severity classes:** 0 = unburnt, or outside the mapped fire extent; 2 = low (burnt
  understorey, unburnt canopy); 3 = moderate (partial canopy scorch); 4 = high (full canopy scorch);
  5 = extreme (full canopy consumption); 255 = nodata. There is no class 1. FESM is itself a
  Sentinel-2 model, so it has its own errors.
- **Land-cover classes (ESA WorldCover 2020)** include 10 = tree cover; 20 = shrubland; 30 = grassland;
  40 = cropland; 50 = built-up; 60 = bare or sparse vegetation; 80 = permanent water;
  90 = herbaceous wetland; 0 = nodata. It was mapped from 2020 imagery but still counts burnt forest
  as tree cover, so treat it as *forest land*, not as a measure of fire damage.

## The glider records

| Column | Meaning |
|---|---|
| `record_id` | ALA record identifier |
| `date`, `year` | When the animal was recorded |
| `latitude`, `longitude` | Location in WGS84 degrees (EPSG:4326). **Reproject to EPSG:3577 before you overlay them on the rasters** |
| `coordinate_uncertainty_m` | How precise the location is, in metres. Most are 10 m, but some old museum records are uncertain by kilometres; filter if that matters |
| `basis_of_record` | `HUMAN_OBSERVATION` or `PRESERVED_SPECIMEN` (museum) |
| `data_provider` | Who supplied the record (mostly NSW BioNet Atlas) |
| `licence` | The record's own licence |

These are presence-only records with uneven survey effort: a count shows where people looked as much
as where gliders live. Records whose licence is non-commercial (CC BY-NC or CC BY-NC-SA) have been
left out of this copy.
