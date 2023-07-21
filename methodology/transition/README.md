# Data Processing: Just Transition

## At home

### Indicator: Fuel poverty
- Data source: [gov.uk: Fuel Poverty trends 2022](https://www.gov.uk/government/statistics/fuel-poverty-trends-2022)
- Preprocessing: [link to script](transition_home.ipynb)
- Reference in locations.json: `transition_home_fuel_poverty`

## At Work

### Indicator: Gender pay gap
- Data from: [ons.gov.uk](https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/datasets/annualsurveyofhoursandearningsashegenderpaygaptables)
- Files: 
   - PROV - Work Region Age Table WGOR Age.12  Gender pay gap 2022
   - PROV - Work Region PubPriv Table 25.12  Gender pay gap 2022 
- Preprocessing: 'extracted relevant fields from the source data file'
- References in locations.json:
  - `gender_pay_gap_ft_age`
  - `gender_pay_gap_ft_sector`
  - `gender_pay_gap_pt_age`
  - `gender_pay_gap_pt_sector`
