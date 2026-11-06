# Check values (workbook Step 7)

Compare the `outputs/severity_summary.csv` that Claude made for you with this table. These numbers
come from a short, separate script written by the presenters
([`presenters/check_values.py`](presenters/check_values.py)), using the same files in `data/`.

## The answers: Tallaganda study area (20 × 20 km = 40,000 ha)

| Fire severity (code) | Area (ha) | Share of the area | Mean NDVI 2019 | 2020 | 2025 | Glider records 2000–2019 | 2020 on | All years |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| unburnt / outside (0) | 19,163 | 47.9 % | 0.62 | 0.71 | 0.65 | 12 | 3 | 21 |
| low (2) | 3,074 | 7.7 % | 0.74 | 0.69 | 0.73 | 10 | 75 | 94 |
| moderate (3) | 5,406 | 13.5 % | 0.75 | 0.64 | 0.73 | 42 | 130 | 210 |
| high (4) | 4,679 | 11.7 % | 0.78 | 0.51 | 0.75 | 63 | 85 | 179 |
| extreme (5) | 7,679 | 19.2 % | 0.74 | 0.34 | 0.71 | 29 | 18 | 47 |

- Burnt (low to extreme): 20,837 ha, which is **52.1 %** of the study area.
- Glider records: **551** in the file, all inside the study area. **156** of them are from 2000–2019.
- Pixels with no data: none in the fire-severity map. In the Sentinel-2 images: 0 in 2019, 1 in 2020
  and 0 in 2025 (they are left out of the NDVI averages).

**How the answers were worked out.**

- Area = number of pixels × 0.01 ha, because each pixel is 10 m × 10 m.
- NDVI = (NIR − red) / (NIR + red), using bands 2 and 1, with no-data pixels (−999) left out.
- Glider records were moved from latitude/longitude onto the images' map grid (EPSG:3577), then
  given the severity class of the pixel they fall in. "2000–2019" means `year` from 2000 to 2019,
  inclusive.

## Yours are different? The usual reasons

| What you see | The likely cause |
|---|---|
| Areas 100 or 10,000 times too big or too small | Wrong pixel area. A 10 m pixel is 100 m², which is 0.01 ha |
| Areas a little too big, or a class code 255 or −999 in the table | No-data pixels were counted as data |
| NDVI above 1 or below −1, or averages that look oddly low | Sentinel-2 no-data (−999) wasn't masked |
| All the glider records in one class, or none on the map | Coordinates weren't converted from latitude/longitude, or longitude and latitude were swapped |
| Glider counts close, but not the same | A different year rule (for example 2000–2020), or a filter on location accuracy. That's fine if `REPORT.md` says so |
| NDVI differs in the second decimal place | Different rounding or masking. Fine if it's explained |

**Something to discuss.** In the *unburnt / outside* class, NDVI goes **up** from 2019 to 2020.
That class isn't all forest: about 60 % of it is grassland in ESA WorldCover 2020 (mostly cleared
grazing land, in the east of the study area) and about 40 % is tree cover. What else changed in
eastern Australia between autumn 2019 and autumn 2020 that could green up pasture? Ask Claude to
split the class by land cover (an extension in the workbook's [More to try](WORKBOOK.md#more-to-try)),
then check its explanation against a source you trust.

**Something else to discuss: what do the glider counts mean?** The *high* class has the most
records from 2000–2019, but the classes differ in size and in how much forest they hold. Per
1,000 ha of tree cover (ESA WorldCover 2020), the records before the fire were:

| Fire severity | Area (ha) | Tree cover | Glider records 2000–2019 on tree cover | Per 1,000 ha of tree cover |
|---|---:|---:|---:|---:|
| unburnt / outside | 19,163 | 40 % | 11 | 1.4 |
| low | 3,074 | 81 % | 10 | 4.0 |
| moderate | 5,406 | 89 % | 41 | 8.5 |
| high | 4,679 | 95 % | 63 | 14.2 |
| extreme | 7,679 | 93 % | 29 | 4.0 |

So, before the fire, gliders were recorded most often in forest that later burnt at high severity.
That tells you about the forest the fire reached, not that gliders favour fire. After the fire,
records jump from 1 in 2019 to 74 in 2020 and 124 in 2024: people went looking. These are
presence-only records (sightings, with no record of where people looked and found none), so a
count shows survey effort as much as where gliders live
([Phillips et al. 2009](https://doi.org/10.1890/07-2153.1)). Keep that in mind for the
*Since the fire* extension.

## Re-create these numbers

```bash
pip install -r requirements.txt
python presenters/check_values.py
```
