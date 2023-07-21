# %%
import pandas as pd
from pathlib import Path
import numpy as np

# %%
# load dataset
DATA_PATH = "https://neeccostorage.blob.core.windows.net/indicatordata/carbon/2005-19_UK_local_and_regional_CO2_emissions.csv"
df = pd.read_csv(
    DATA_PATH,
    delimiter=",",
    header=0,
)
# %%
# select columns you want to pivot longer
columns = list(df.columns)
not_to_pivot = columns[0:5]
to_pivot = columns[5:]

# %%
# pivot longer
df_long = pd.melt(
    df,
    id_vars=not_to_pivot,
    value_vars=to_pivot,
    value_name="metric",
    ignore_index=False,
)
# %%
# format columns headers: make lower case
df_long.columns = df_long.columns.str.lower()
# remove spaces and /
df_long.columns = df_long.columns.map(lambda x: x.replace(" ", "_").replace("/", "_"))
# %%
# filter df_long for the right regions and metrics
local_authorities = (
    "Darlington",
    "County Durham",
    "Gateshead",
    "Hartlepool",
    "Middlesbrough",
    "Newcastle upon Tyne",
    "North Tyneside",
    "Northumberland",
    "Redcar and Cleveland",
    "South Tyneside",
    "Stockton-on-Tees",
    "Sunderland",
)

co2_ne_la = df_long.query(
    "local_authority in @local_authorities and variable == 'Per Capita Emissions (t)'"
)

# %%
# select columns and rename metric
column_list = ["local_authority", "year", "metric"]
co2_ne_la = co2_ne_la[co2_ne_la.columns.intersection(column_list)]
co2_ne_la = co2_ne_la.rename(columns={"metric": "Per Capita Emissions (tonnes)"})


# %%
TVCA = [
    "Darlington",
    "Hartlepool",
    "Middlesbrough",
    "Redcar and Cleveland",
    "Stockton-on-Tees",
]
NECA = [
    "County Durham",
    "Gateshead",
    "Newcastle upon Tyne",
    "North Tyneside",
    "Northumberland",
    "South Tyneside",
    "Sunderland",
]

co2_ne_la["Region"] = np.select(
    [co2_ne_la.local_authority.isin(NECA), co2_ne_la.local_authority.isin(TVCA)],
    ["NECA", "TVCA"],
    default="NECA",
)


# %%
co2_ne_la = co2_ne_la.rename(
    columns={"local_authority": "Local Authority", "year": "Year"}
)
co2_ne_la["Year"] = co2_ne_la["Year"].astype(int)
co2_ne_la = co2_ne_la[
    ["Local Authority", "Region", "Year", "Per Capita Emissions (tonnes)"]
]

# %%
co2_ne_la.to_csv("carbon_la_CO2_emission_estimates_2005-2019.csv")

# %%