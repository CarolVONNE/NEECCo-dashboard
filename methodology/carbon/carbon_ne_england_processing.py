# %%
import pandas as pd

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
local_authorities = ("England Total", "North East Total")
co2_ne_eng = df_long.query(
    "local_authority in @local_authorities and variable == 'Per Capita Emissions (t)'"
)

# %%
# select columns and rename metric
column_list = ["region_country", "year", "metric"]
co2_ne_eng = co2_ne_eng[co2_ne_eng.columns.intersection(column_list)]
co2_ne_eng = co2_ne_eng.rename(columns={"metric": "Per Capita Emissions (tonnes)"})

# %%
co2_ne_eng.to_csv("ne_and_england_co2_totals.csv")

# %%