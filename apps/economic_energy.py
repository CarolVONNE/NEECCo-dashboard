import plotly.graph_objects as go
import pandas as pd

import dash
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

from app import app, neecco_palette

from locations_loader import LocationsLoader

# data
locations = LocationsLoader()
gas_electric = pd.read_csv(locations.get_link("economic_energy_gas_electric"))
total = pd.read_csv(locations.get_link("economic_energy_total"))
renewables = pd.read_csv(locations.get_link("economic_energy_renewables"))

# figs
fig_gas_electric = px.line(
    gas_electric,
    x="year",
    y="value",
    color="type",
    line_dash="region",
    markers=True,
    color_discrete_sequence=neecco_palette,
    template="simple_white",
    labels={
        "year": "Year",
        "value": "kw per meter",
        "type": "Type",
        "region": "Region",
    },
)
fig_gas_electric.update_traces(
    patch={"line": {"dash": "dot"}}, selector={"legendgroup": "Electric, GB Total"}
)
fig_gas_electric.update_traces(
    patch={"line": {"dash": "solid"}}, selector={"legendgroup": "Electric, North East"}
)
fig_gas_electric.update_traces(
    patch={"line": {"dash": "dot"}}, selector={"legendgroup": "Gas, GB Total"}
)
fig_gas_electric.update_traces(
    patch={"line": {"dash": "solid"}}, selector={"legendgroup": "Gas, North East"}
)


fig_total = px.line(
    total,
    x="year",
    y="value",
    color="type",
    line_dash="region",
    markers=True,
    color_discrete_sequence=neecco_palette,
    template="simple_white",
    labels={"year": "Year", "value": "ktoe", "type": "Type", "region": "Region"},
)
fig_total.update_traces(
    patch={"line": {"dash": "dot"}}, selector={"legendgroup": "Domestic, GB Total"}
)
fig_total.update_traces(
    patch={"line": {"dash": "solid"}}, selector={"legendgroup": "Domestic, North East"}
)
fig_total.update_traces(
    patch={"line": {"dash": "dot"}}, selector={"legendgroup": "Transport, GB Total"}
)
fig_total.update_traces(
    patch={"line": {"dash": "solid"}}, selector={"legendgroup": "Transport, North East"}
)
fig_total.update_traces(
    patch={"line": {"dash": "dot"}}, selector={"legendgroup": "Commercial, GB Total"}
)
fig_total.update_traces(
    patch={"line": {"dash": "solid"}},
    selector={"legendgroup": "Commercial, North East"},
)


fig_renewables = px.line(
    renewables,
    x="year",
    y="value",
    line_dash="region",
    markers=True,
    color_discrete_sequence=neecco_palette,
    template="simple_white",
    labels={"year": "Year", "value": "MW", "region": "Region"},
)

title = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H1("Economic: Energy", className="py-3")])]),
        dbc.Row(
            html.P(
                "The generation of energy underpins much of our lives at work and home. Decarbonizing energy production needs to be met with reducing overall demand, which includes increased efficiency. Some advocate that more dispersed energy production addresses significant inefficiency in our current system as well as making our energy networks resilient to changing climate and weather patterns."
            )
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4("Page Content"),
                        html.Ul(
                            [
                                html.Li(
                                    html.A(
                                        html.P("Renewables in the region"),
                                        href="#section1",
                                    )
                                ),
                                html.Li(
                                    html.A(
                                        html.P("Total energy consumption"),
                                        href="#section2",
                                    )
                                ),
                                html.Li(
                                    html.A(
                                        html.P(
                                            "Regional consumption of gas and electricity"
                                        ),
                                        href="#section3",
                                    )
                                ),
                                html.Li(
                                    html.A(
                                        html.P("Energy in the community"),
                                        href="#section4",
                                    )
                                ),
                            ]
                        ),
                    ]
                )
            ]
        ),
    ],
    class_name="container-type1",
)

renewables = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                [
                    html.H2("Renewables in the region"),
                ]
            )
        ),
        dbc.Row(
            dbc.Col(
                [
                    html.H5("Total installed renewable generation capacity"),
                    dcc.Graph(
                        id="grph3",
                        figure=fig_renewables,
                        config={
                            "displayModeBar": True,
                            "modeBarButtonsToRemove": [
                                "lasso2d",
                                "select2d",
                                "autoScale2d",
                                "zoom2d",
                                "pan2d",
                                "toImage",
                            ],
                            "displaylogo": False,
                        },
                    ),
                    html.A(
                        "Data Source: The UK Government website",
                        href="https://www.gov.uk/government/statistics/regional-renewable-statistics",
                        target="_blank",
                    ),
                ]
            ),
        ),
    ],
    id="section1",
    class_name="container-type1",
)

total = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                [
                    html.H2("Total energy consumption"),
                ]
            )
        ),
        dbc.Row(
            dbc.Col(
                [
                    html.H5("Total consumption by type"),
                    dcc.Graph(
                        id="grph1",
                        figure=fig_total,
                        config={
                            "displayModeBar": True,
                            "modeBarButtonsToRemove": [
                                "lasso2d",
                                "select2d",
                                "autoScale2d",
                                "zoom2d",
                                "pan2d",
                                "toImage",
                            ],
                            "displaylogo": False,
                        },
                    ),
                    html.A(
                        "Data Source: The UK Government website",
                        href="https://www.gov.uk/government/statistics/total-final-energy-consumption-at-regional-and-local-authority-level-2005-to-2019",
                        target="_blank",
                    ),
                ]
            ),
        ),
    ],
    id="section2",
    class_name="container-type1",
)

gas_electric = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                [
                    html.H2("Regional consumption of gas and electricity"),
                ]
            )
        ),
        dbc.Row(
            dbc.Col(
                [
                    html.H5("Mean consumption"),
                    dcc.Graph(
                        id="grph2",
                        figure=fig_gas_electric,
                        config={
                            "displayModeBar": True,
                            "modeBarButtonsToRemove": [
                                "lasso2d",
                                "select2d",
                                "autoScale2d",
                                "zoom2d",
                                "pan2d",
                                "toImage",
                            ],
                            "displaylogo": False,
                        },
                    ),
                    html.A(
                        "Data Source: The UK Government website",
                        href="https://www.gov.uk/government/statistics/regional-and-local-authority-gas-consumption-statistics",
                        target="_blank",
                    ),
                ]
            ),
        ),
    ],
    id="section3",
    class_name="container-type1",
)

community = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                [
                    html.H2("Energy in the community"),
                ]
            )
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Iframe(
                            src="https://www.google.com/maps/d/embed?mid=1xc4LV7wUm5q47krpKLUyF-KkyGOg8WU8&ehbc=2E312F",
                            width="100%",
                            height="630px",
                        ),
                        html.A(
                            [html.P("Northern Powergrid Communities")],
                            href="https://www.google.com/maps/d/edit?mid=1xc4LV7wUm5q47krpKLUyF-KkyGOg8WU8&ll=54.54965039558909%2C-2.7223892122056714&z=8",
                            target="_blank",
                        ),
                    ],
                    xs=12,
                    sm=12,
                    md=12,
                    lg=6,
                    xl=6,
                ),
                dbc.Col(
                    [
                        html.Iframe(
                            src="https://www.google.com/maps/d/embed?mid=1zGQXlC3lM3uEkZeML5iFQx6fCoJpJUgP&ehbc=2E312F&ll=54.93408021162525%2C-1.4117425731715638&z=9&ehbc=2E312F",
                            width="100%",
                            height="630px",
                        ),
                        html.A(
                            [html.P("Community Energy England")],
                            href="https://www.google.com/maps/d/u/0/viewer?mid=1zGQXlC3lM3uEkZeML5iFQx6fCoJpJUgP&ll=54.85559004609846%2C-1.0610453063144565&z=9",
                            target="_blank",
                        ),
                        html.Img(
                            src="assets/sidebar.ico",
                            style={"display": "inline"},
                            height="20px",
                        ),
                        html.P(
                            " Click this icon above to open the sidebar and select the following to see more:",
                            style={"display": "inline"},
                        ),
                        html.Ul(
                            [
                                html.Li("1_Non-RCEF projects and programme"),
                                html.Li("2_RCEF projects and programme"),
                            ]
                        ),
                        html.P("Click the icon again to close the sidebar."),
                    ],
                    xs=12,
                    sm=12,
                    md=12,
                    lg=6,
                    xl=6,
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(["See also:"]),
                        html.A(
                            "Northern Powergrid - Community Energy",
                            href="https://www.northernpowergrid.com/community-energy",
                            target="_blank",
                        ),
                    ]
                ),
                html.A(
                    "Community Energy England - State of the Sector Report 2022 (pdf)",
                    href="https://communityenergyengland.org/files/document/626/1655376945_CommunityEnergyStateoftheSectorUKReport2022.pdf",
                    target="_blank",
                ),
            ]
        ),
    ],
    id="section4",
    class_name="container-type1",
)

layout = dbc.Container(
    [dbc.Row([dbc.Col([title, renewables, total, gas_electric, community])])]
)
