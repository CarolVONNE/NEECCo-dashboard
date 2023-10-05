import plotly.graph_objects as go
import pandas as pd

import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import plotly.express as px

from app import app, neecco_palette

from locations_loader import LocationsLoader

# initialise locations loader
locations = LocationsLoader()

# read data
df1 = pd.read_csv(locations.get_link("carbon_CO2_ne_england"), delimiter=",", header=0)

df2 = pd.read_csv(locations.get_link("carbon_CO2_la"), delimiter=",", header=0)

df3 = pd.read_csv(locations.get_link("carbon_greenhouse_gas"), delimiter=",", header=0)
df4 = pd.read_csv(
    locations.get_link("carbon_pathway_projections"), delimiter=",", header=0
)
carbon_per_capita_LA_df = pd.read_csv(
    locations.get_link("carbon_per_capita_LA"), delimiter=","
)

# create figures
fig1 = px.line(
    df1,
    x="Year",
    y="Per Capita Emissions (tonnes)",
    template="simple_white",
    line_dash="Region",
    markers=True,
    color_discrete_sequence=neecco_palette,
)

fig2 = px.line(
    df2,
    x="Year",
    y="Per Capita Emissions (tonnes)",
    template="simple_white",
    color="Region",
    line_dash="Local Authority",
    markers=True,
    color_discrete_sequence=neecco_palette[0:2],
)

fig3 = px.line(
    df3,
    x="Year",
    y="Greenhouse gas emissions (MtCO2e)",
    template="simple_white",
    color="Gas",
    markers=True,
    color_discrete_sequence=neecco_palette,
)
fig3.update_layout(
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)


fig4 = px.line(
    df4,
    x="Year",
    y="Mt CO2",
    template="simple_white",
    color="Category",
    markers=False,
    color_discrete_map={
        "Historical Pathway": "#669900",
        "Recommended Pathway": "#60A0C8",
        "Recorded Total Emission Estimates": "#D83731",
    }
)
fig4.update_layout(
    legend=dict(
        orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, title=""
    )
)

# Sections

# Section 1: page title
title = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H1("Carbon", className="py-3")])]),
        dbc.Row(
            [
                html.P(
                    [
                        "The Intergovernmental Panel on Climate Change is the United Nations body for assessing the science related to climate change.",
                        html.Span(
                            [
                                html.A(
                                    "https://www.ipcc.ch/",
                                    href="https://www.ipcc.ch/",
                                    target="_blank",
                                )
                            ]
                        ),
                        " In March 2023 it stated: “There are multiple, feasible and effective options to reduce greenhouse gas emissions and adapt to human-caused climate change, and they are available now…“ In 2018, IPCC highlighted the unprecedented scale of the challenge required to keep warming to 1.5°C. Five years later, that challenge has become even greater due to a continued increase in greenhouse gas emissions. The pace and scale of what has been done so far, and current plans, are insufficient to tackle climate change. ",
                    ]
                ),
                html.P(
                    [
                        "The UK’s Climate Change Committee (CCC) is an independent, statutory body that advises governments on emissions targets and reports to Parliament ",
                        html.Span(
                            [
                                html.A(
                                    "https://www.theccc.org.uk/",
                                    href="https://www.theccc.org.uk/",
                                    target="_blank",
                                )
                            ]
                        ),
                        ". In June 2023 it stated “Our confidence in the UK meeting its goals from 2030 onwards is now markedly less than it was in our previous assessment a year ago.“",
                    ]
                ),
                html.P(
                    [
                        "Although there is a focus on carbon dioxide there are also other gases that cause the ‘green house effect’ including methane and nitrous oxide. If this is new to you, you will find some useful information here: ",
                        html.Span(
                            [
                                html.A(
                                    "https://www.goinggreentogether.org/learn",
                                    href="https://www.goinggreentogether.org/learn",
                                    target="_blank",
                                )
                            ]
                        ),
                    ]
                ),
            ]
        ),
        dbc.Row(
            dbc.Col(
                [
                    html.H4("Page Content"),
                    html.Ul(
                        [
                            html.Li(
                                html.A(
                                    html.P(
                                        "Climate Clock: Deadline to Zero Carbon Emissions"
                                    ),
                                    href="#section1",
                                )
                            ),
                            html.Li(
                                html.A(
                                    html.P("Greenhouse Effect"),
                                    href="#section2",
                                )
                            ),
                            html.Li(
                                html.A(
                                    html.P("Carbon Budget for the North East"),
                                    href="#section3",
                                )
                            ),
                            html.Li(
                                html.A(
                                    html.P(
                                        "North East CO2 emissions estimates per capita"
                                    ),
                                    href="#section4",
                                )
                            ),
                            html.Li(
                                html.A(
                                    html.P(
                                        "Estimated greenhouse gas emissions for the UK"
                                    ),
                                    href="#section5",
                                )
                            ),
                        ]
                    ),
                ]
            ),
        ),
    ],
    class_name="container-type1",
)


# Section 2: content
content = dbc.Container(
    [],
    class_name="container-type1",
)


# Section 3: carbon clock
carbon_clock = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1(
                            "Climate Clock: Deadline to Zero Carbon Emissions",
                            className="py-3",
                        ),
                        html.Iframe(
                            srcDoc="<script src='https://climateclock.world/widget-v2.js' async></script><climate-clock />",
                            style={"width": "100%"},
                        ),
                        html.P(
                            html.A(
                                "Source: climateclock.world",
                                href="https://climateclock.world",
                                target="_blank",
                            )
                        ),
                    ]
                )
            ]
        )
    ],
    id="section1",
    class_name="container-type1",
)

# Section 3: carbon clock
greenhouse_effect = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1(
                            "Greenhouse Effect",
                            className="py-3",
                        ),
                        html.P(
                            "A diagram created by Dr. Elder, National Park Services (U.S. Department of Interior), to help communicate climate change."
                        ),
                        html.A(
                            [
                                html.Img(
                                    src=locations.get_link(
                                        "carbon_national_park_service"
                                    ),
                                    width="95%",
                                )
                            ],
                            href=locations.get_link("carbon_national_park_service"),
                            target="_blank",
                        ),
                        html.P(
                            html.A(
                                "Source: National Park Services (U.S. Department of Interior)",
                                href="https://www.nps.gov/goga/learn/nature/climate-change-causes.htm",
                                target="_blank",
                            )
                        ),
                    ]
                )
            ]
        )
    ],
    id="section2",
    class_name="container-type1",
)


# Section 4: Carbon Budget
carbon_budget = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Carbon Budget for the North East"),
                        html.H5(
                            "Pathway projections for the North East and recorded total emission estimates"
                        ),
                        dcc.Graph(
                            id="grph4",
                            figure=fig4,
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
                        html.P(
                            html.A(
                                "Data Source: Tyndall Centre for Climate Change Research",
                                href="https://carbonbudget.manchester.ac.uk/reports/NE/",
                                target="_blank",
                            )
                        ),
                        
                    ],
                    align="centre",
                )
            ]
        )
    ],
    id="section3",
    class_name="container-type1",
)


# Section 3: North East CO2 emission estimates per capita
CO2_emissions = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("North East CO2 emissions estimates per capita"),
                        html.H5(
                            "CO2 emissions estimates from 2005-2019 for the North East and England"
                        ),
                        dcc.Graph(
                            id="grph1",
                            figure=fig1,
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
                        html.P(
                            html.A(
                                "Data Source: Department for Business, Energy & Industrial Strategy",
                                href="https://www.gov.uk/government/statistics/uk-local-authority-and-regional-carbon-dioxide-emissions-national-statistics-2005-to-2019",
                                target="_blank",
                            )
                        ),
                    ],
                    align="centre",
                )
            ]
        )
    ],
    id="section4",
    class_name="container-type1",
)


# Section 5: Estimated territorial greenhouse gas emissions by gas, by million tonnes carbon dioxide equivalent (MtCO2e), UK 1990-2020
greenhouse_gas = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Estimated greenhouse gas emissions for the UK"),
                        html.H5(
                            "Estimated territorial greenhouse gas emissions, by gas, by million tonnes carbon dioxide equivalent (MtCO2e), UK 1990-2020"
                        ),
                        dcc.Graph(
                            id="grph3",
                            figure=fig3,
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
                            "Data Source: Department for Business, Energy & Industrial Strategy",
                            href="https://www.gov.uk/government/statistics/final-uk-greenhouse-gas-emissions-national-statistics-1990-to-2020",
                            target="_blank",
                        ),
                        html.H5(
                            "Local Authority territorial CO2 emissions estimates 2005-2019 per capita - annual change (%)",
                            style={"padding-top": "20px"},
                        ),
                        dash_table.DataTable(
                            carbon_per_capita_LA_df.to_dict("records"),
                            [
                                {"name": i, "id": i}
                                for i in carbon_per_capita_LA_df.columns
                            ],
                            style_table={"overflowY": "auto"},
                            style_header={
                                "backgroundColor": "#669900",
                                "color": "white",
                                "font-weight": "bold",
                            },
                            id="tbl",
                        ),
                        html.A(
                            "Data Source: Department for Business, Energy & Industrial Strategy",
                            href="https://www.gov.uk/government/statistics/final-uk-greenhouse-gas-emissions-national-statistics-1990-to-2020",
                            target="_blank",
                        ),
                    ],
                    align="centre",
                )
            ]
        )
    ],
    id="section5",
    class_name="container-type1",
)

# create layout
layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        title,
                        carbon_clock,
                        greenhouse_effect,
                        carbon_budget,
                        CO2_emissions,
                        greenhouse_gas,
                    ]
                )
            ]
        ),
    ]
)
