import plotly.graph_objects as go
import pandas as pd

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import plotly.express as px

from app import app, neecco_palette

from locations_loader import LocationsLoader

# data
locations = LocationsLoader()

# read data
df1 = pd.read_csv(locations.get_link("economic_circular_UK_env_EGSS"))
df2 = pd.read_csv(locations.get_link("economic_circular_waste_recycling"))

# create figures
fig1 = px.line(
    df1,
    x="Year",
    y="£ million",
    template="simple_white",
    markers=True,
    color_discrete_sequence=neecco_palette,
)

fig2 = px.line(
    df2,
    x="Year",
    y="Household Recycling Rates",
    line_dash="Region",
    template="simple_white",
    markers=True,
    color_discrete_sequence=neecco_palette,
)

# Sections

# Section: page title
title = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [html.H1("Economic: Towards A Circular Economy ", className="py-3")]
                )
            ]
        ),
        dbc.Row(
            [
                html.P(
                    [
                        "A good introduction to the idea of a circular economy can be found here ",
                        html.Span(
                            [
                                html.A(
                                    "https://ellenmacarthurfoundation.org/topics/circular-economy-introduction/overview",
                                    href="https://ellenmacarthurfoundation.org/topics/circular-economy-introduction/overview",
                                )
                            ]
                        ),
                        " - Many others are available! While this may be the direction we need to move, at this stage there is national data on a specific industrial sector delivering environmental goods and services. This includes recycling. With local authorities having specific duties about the recycling of household waste there is considerable data. In some parts of the private sector such information is considered commercially sensitive.",
                    ]
                ),
                html.P(
                    "Our futures include addressing our industrial heritage, much of which within the North East is – as it was - underground. The ‘constraints map’ was developed when this was seen solely as a problem that needed to be worked around. In more recent years the potential to use the heat of mine water is being explored. Historic landfill sites present a different, perhaps greater challenge. "
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
                                        "First estimates of the UK Environmental goods and services sector (EGSS)"
                                    ),
                                    href="#section1",
                                )
                            ),
                            html.Li(
                                html.A(html.P("Waste recycling"), href="#section2")
                            ),
                            html.Li(
                                html.A(
                                    html.P("Mining and ground water constraints"),
                                    href="#section3",
                                )
                            ),
                            html.Li(
                                html.A(
                                    html.P("Historical Landfill Sites"),
                                    href="#section4",
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

# Section: First estmates of the UK environmental goods and services sector (EGSS)
EGSS_content = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                [
                    html.H2(
                        "First estimates of the UK environmental goods and services sector (EGSS)"
                    ),
                    html.H5(
                        "Total environmental goods and services sector: output by activity, UK, 2010 to 2019"
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
                    html.A(
                        "Data Source: The Office for National Statistics",
                        href="https://www.ons.gov.uk/economy/environmentalaccounts/datasets/ukenvironmentalgoodsandservicessectoregssestimates",
                        target="_blank",
                    ),
                ],
                align="centre",
            )
        ),
    ],
    id="section1",
    class_name="container-type1",
)

# Section: Waste recycling
waste_recycling = dbc.Container(
    dbc.Row(
        dbc.Col(
            [
                html.H2("Waste recycling"),
                html.H5(
                    "Regional household recycling rates 2000-01 to 2020-21 for the North East and England"
                ),
                dcc.Graph(
                    id="grph2",
                    figure=fig2,
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
                    href="https://www.gov.uk/government/statistical-data-sets/env18-local-authority-collected-waste-annual-results-tables ",
                    target="_blank",
                ),
            ]
        )
    ),
    id="section2",
    class_name="container-type1",
)


# Section: Mining and ground water constraints
mining_ground_water = dbc.Container(
    [
        dbc.Row([html.H2("Mining and ground water constraints")]),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.A(
                            [
                                html.Img(
                                    src=locations.get_link(
                                        "economic_circular_mining_and_groundwater_constraints"
                                    ),
                                    width="100%",
                                )
                            ],
                            href="https://environment.data.gov.uk/dataset/aad0aa76-cbab-4356-ad62-1ecfb6a619ac",
                            target="_blank",
                        ),
                        html.A(
                            "Data Source: Department for Environment, Food & Rural Affairs",
                            href="https://environment.data.gov.uk/dataset/aad0aa76-cbab-4356-ad62-1ecfb6a619ac",
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
                            src="https://mapapps2.bgs.ac.uk/coalauthority/home.html",
                            width="100%",
                            height="528 px",
                        ),  # fix height to size of image in left hand column
                    ],
                    xs=12,
                    sm=12,
                    md=12,
                    lg=6,
                    xl=6,
                ),
            ]
        ),
    ],
    id="section3",
    class_name="container-type1",
)

# Section: Historic Landfill Sites
historic_landfill_sites = dbc.Container(
    [
        dbc.Row([html.H2("Historic Landfill Sites")]),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Iframe(
                                    src=locations.get_link(
                                        "economic_circular_landfill_map"
                                    ),
                                    width="100%",
                                    height="750",
                                )
                            ]
                        ),
                        html.A(
                            "Source: Department for Environment Food & Rural Affairs",
                            href="https://environment.data.gov.uk/DefraDataDownload/?mapService=EA/HistoricLandfill&Mode=spatial ",
                            target="_blank",
                        ),
                    ]
                )
            ]
        ),
    ],
    id="section4",
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
                        EGSS_content,
                        waste_recycling,
                        mining_ground_water,
                        historic_landfill_sites,
                    ]
                )
            ]
        )
    ]
)
