## Data Processing: Economic
## Circular

### Indicator: First estimates of the UK environmental goods and services sector (EGSS)
- Data from: [ons.gov.uk](https://www.ons.gov.uk/economy/environmentalaccounts/datasets/ukenvironmentalgoodsandservicessectoregssestimates)
- Tab: Output by activity
- Table name: Environmental goods and services sector: output by activity, UK, 2010 to 2019
- Reference in locations.json: `economic_circular_UK_env_EGSS`

### Indicator: Waste recycling
- Data from: [gov.uk](https://www.gov.uk/government/statistical-data-sets/env18-local-authority-collected-waste-annual-results-tables (Local authority collected waste generation from April 2000 to March 2021 (Englang and regions) and local authority data April 2020 to March 2021))
- Tab: Table_3a
- Table name: Table 3a: Regional Household Recycling Rates 2000-01 to 2020-21
- Reference in locations.json: `economic_circular_waste_recycling`

### Indicator: North East Mining and Groundwater Constraints Map
- Link to: [data.gov.uk](https://environment.data.gov.uk/dataset/aad0aa76-cbab-4356-ad62-1ecfb6a619ac)
- Screenshot from: [data.gov.uk](https://environment.data.gov.uk/dataset/aad0aa76-cbab-4356-ad62-1ecfb6a619ac)
- Reference in locations.json: `economic_circular_mining_and_groundwater_constraints`

### Indicator: Landfill sites
- Data from: [DEFRA Data Services Platform](https://environment.data.gov.uk/DefraDataDownload/?mapService=EA/HistoricLandfill&Mode=spatial)
- Preprocessing: [landfill_data_map_export.py](./landfill_data_map_export.py)
- Reference in locations.json: `economic_circular_landfill_map`

## Energy

### Indicator: Renewables in the region
- Data from: [service.gov.uk](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1107330/Renewable_electricity_-_installed_capacity_by_region_2003_-_2021.xls)
- Tab: All yearly tabs, using totals for North East and UK Total
- Table name: Installed capacity of sites generating electricity from renewable sources
- Preprocessing: [energy.ipynb](./energy.ipynb)
- Reference in locations.json: `economic_energy_renewables`

### Indicator: Total energy consumption
- Data from: [service.gov.uk](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1043596/subnational_total_final_energy_consumption_2019.xlsx)
- Tab: All yearly tabs, 'All fuels: Domestic', 'All fuels" Transport', 'All fuels: Industrial, Commercial and other' for Great Britain and North East
- Table name: Subnational total final energy consumption (ktoe), United Kingdom
- Reference in locations.json: `economic_energy_total`

### Indicator: Regional consumption of gas and electricity
- Data from: 
    - [service.gov.uk](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1126184/subnational_gas_consumption_statistics_2005-2021.xlsx)
    - [service.gov.uk](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1126137/subnational_electricity_consumption_statistics_2005-2021.xlsx)
- Tab: All yearly tabs, "Mean consumption (kWh per meter): All meters" for North East and Great Britain
- Table name: Subnational electricity consumption, Great Britain
- Preprocessing: [energy.ipynb](./energy.ipynb)
- Reference in locations.json: `economic_energy_gas_electric`

### Indicator: Energy in the community
- Screenshot from: [Northern powergrid](https://www.northernpowergrid.com/community-energy)
- Reference in locations.json: `economic_energy_northern_powergrid`

## Also

### Indicator: TVCA and NELEP evidence hubs
- Links to: 
    - [Tees Valley CA](https://teesvalley-ca.gov.uk/InstantAtlas/Tees_Valley_Data_Insights/atlas.html)
    - [Evidence hub](https://evidencehub.northeastlep.co.uk/)

### Indicator: International connectivity
- Links to: 
    - [dft.gov.uk](https://maps.dft.gov.uk/maritime-statistics/index.html)
    - [Teeside International](https://www.teessideinternational.com/about-us/)
    - [Newcastle Airport](https://www.newcastleairport.com/about-your-airport/environment/net-zero-carbon-2035/)
- Screenshot from:
    - [dft.gov.uk](https://maps.dft.gov.uk/maritime-statistics/index.html)
- Reference in locations.json: `economic_also_maritime_statistics`