# Data Processing: Nature

## Land

### Indicator: National Character Area profiles
- Data from: [data.gov.uk](https://www.data.gov.uk)
- Link: [National Character Areas (England)](https://www.data.gov.uk/dataset/21104eeb-4a53-4e41-8ada-d2d442e416e0/national-character-areas-england)
- Reference in locations.json: `nature_land_landscape_shapefile`
- Preprocessing: [nature_land_landscape_profiles.ipynb](./nature_land_landscape_profiles.ipynb)
- Reference in locations.json: `nature_land_landscape_folium_map`

## Water

### Indicator: Fish Counts
- Data from: 
    - [gov.uk (Wear)](https://www.gov.uk/government/statistical-data-sets/river-wear-upstream-fish-counts)
    - [gov.uk (Tyne)](https://www.gov.uk/government/statistical-data-sets/river-tyne-fish-counts)
    - [gov.uk (Tees)](https://www.gov.uk/government/statistical-data-sets/river-tees-upstream-fish-counts)
- Tab: monthly_counts/monthly_counts_combined
- Preprocessing: [water_fish_counts.ipynb](./water_fish_counts.ipynb)
- Reference in locations.json: `natural_water_fish`

### Indicator: River Basin Management

- Links to: 
    - [data.gov.uk](https://environment.data.gov.uk/catchment-planning/RiverBasinDistrict/3)
    - [data.gov.uk](https://environment.data.gov.uk/DefraDataDownload/?mapService=EA/RiskOfFloodingFromRiversAndSea&Mode=spatial)
- Screenshots from:
    - [data.gov.uk](https://environment.data.gov.uk/catchment-planning/RiverBasinDistrict/3)
    - [data.gov.uk](https://environment.data.gov.uk/DefraDataDownload/?mapService=EA/RiskOfFloodingFromRiversAndSea&Mode=spatial)
- Reference in locations.json: `nature_water_river_basin`, `nature_water_flooding`
  
## Also

### Indicator: Clean Air

- Links to:
  - [defra.gov.uk](https://uk-air.defra.gov.uk/data/gis-mapping/)
  - [Clean air hub](https://www.cleanairhub.org.uk/home)
  - [defra.gov.uk](https://uk-air.defra.gov.uk/forecasting/locations?q=north+east+england)

### Indicator: National Atlases and Repositories

- Screenshot provided by NEECCo
- Links to:
  - [ERIC](https://www.ericnortheast.org.uk/)
  - [Countryside Survey](https://countrysidesurvey.org.uk/about)
  - [NBN atlas](https://nbnatlas.org/)
- Reference in locations.json: `nature_also_biodiversity`

### Indicator: Changing Weather
- Data from: [UK Met Office](https://www.metoffice.gov.uk/)
- Link: [https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data](https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data)
- Region: 'Durham'
- Preprocessing: [natural_changing_weather.ipynb](./natural_changing_weather.ipynb)
- Reference in locations.json: `natural_and_also_changing_weather`