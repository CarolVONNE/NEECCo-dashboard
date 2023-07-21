# Data Processing: Carbon

## Carbon Budget for the North East
### Indicator: Pathway projections for the North East and recorded total emission estimates
Data Source 1: [Tyndall Centre for Climate Change Research](https://carbonbudget.manchester.ac.uk/reports/NE/)  
Data Source 2: [UK, Local-Authority and Regional Carbon Dioxide Emissions, www.gov.uk](https://www.gov.uk/government/statistics/uk-local-authority-and-regional-carbon-dioxide-emissions-national-statistics-2005-to-2019)  
Preprocessing: Manually extracted pathway projections from data source 1 and combined with the North East values manually extracted from data source 2.  
Reference in locations.json: 'carbon_pathway_projections'   

## North East CO2 emissions estimates per capita
### Indicator: CO2 emissions estimates from 2005-2019 for the North East and England
Data Source: [UK, Local-Authority and Regional Carbon Dioxide Emissions, www.gov.uk](https://www.gov.uk/government/statistics/uk-local-authority-and-regional-carbon-dioxide-emissions-national-statistics-2005-to-2019)   
Preprocessing: carbon_ne_england_processing.py   
Reference in locations.json: 'carbon_CO2_ne_england'  

## Estimated greenhouse gas emissions for the UK   
### Indicator: Estimated territorial greenhouse gas emissions, by gas, by million tonnes carbon dioxide equivalent (MtCO2e), UK 1990-2020   
Data Source: [Final UK Greenhouse Gas Emissions, www.gov.uk](https://www.gov.uk/government/statistics/final-uk-greenhouse-gas-emissions-national-statistics-1990-to-2020)  
Preprocessing: Extracted relevant fields from the source data file   
Reference in locations.json: 'carbon_greenhouse_gas'  

### Indicator: Local Authority territorial CO2 emissions estimates 2005-2019 per capita - annual change (%)   
Data Source: [UK, Local-Authority and Regional Carbon Dioxide Emissions, www.gov.uk](https://www.gov.uk/government/statistics/uk-local-authority-and-regional-carbon-dioxide-emissions-national-statistics-2005-to-2019)  
Preprocessing: 
- Run 1st, extracts only relevant variables: [carbon_ne_la_processing.py](./carbon_ne_la_processing.py)
- Calcualate annual change in %: [carbon_per_capita_LA.ipynb](./carbon_per_capita_LA.ipynb)
Reference in locations.json: 'carbon_per_capita_LA'