# Data Processing: Social

## Our Communities


### Indicator: Poverty

- Data source: [ons.gov.uk](https://www.ons.gov.uk/economy/regionalaccounts/grossdisposablehouseholdincome/bulletins/regionalgrossdisposablehouseholdincomegdhi/1997to2019#gross-disposable-household-income-for-itl3-local-areas)
- Preprocessing: [link to script](communities.ipynb)
- Reference in locations.json: `social_communities_gdhi`

### Indicator: Free school meals
- Data source: [gov.uk](https://explore-education-statistics.service.gov.uk/find-statistics/school-pupils-and-their-characteristics#dataBlock-87182242-6c3a-4eb1-b5fc-d91da60207e9-charts)
- Preprocessing: [link to script](transition_also.ipynb)
- Reference in locations.json: `transition-also-fsm`

## Engagement with Nature
### Indicator: Third sector organisations contribution to the environment
- Data source: email sent from contact who contributes to the [Community Foundation Third Sector Trends Survey](https://www.communityfoundation.org.uk/third-sector-trends/ )
- Preprocessing: 'extracted relevant fields from the source data file'
- Reference in locations.json: `social_nature_third_sector_trends_impact_on_local_env`


### Indicator: Key regional grant funders
- Data source: [Funding Information North East (FINE) directory](https://www.vonne.org.uk/funding)
- Preprocessing: 'extracted relevant fields from the source data file'
- Reference in locations.json: `social_nature_funders`

## Also

### Indicator: Number of trips by mode
- Data source: [gov.uk](https://www.gov.uk/government/statistical-data-sets/nts03-modal-comparisons)
- File name: NTS9903
- Preprocessing: [link to script](also.ipynb)
- Reference in locations.json: `social_also_trips`

### Indicator: Walking and cycling
- Data source: [gov.uk](https://www.gov.uk/government/statistical-data-sets/nts03-modal-comparisons)
- File name: CW0301
- Preprocessing: [link to script](also.ipynb)
- Reference in locations.json: `social_also_active_travel`
