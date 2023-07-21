import plotly.graph_objects as go
import pandas as pd

import dash
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

#### Row 1: Towards a circular economy
economic_circular = dbc.CardGroup(
    dbc.Card(
        [dbc.CardBody(html.H4(children="Towards a circular economy"))],
        outline=True,
        className="py-2 border-success",
    ),
    className="mb-2",
)

card00 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5(
                    "(20) First estimates of the UK environmental goods and services sector (EGSS)",
                    className="card-title",
                ),
                html.I(
                    className="bi bi-arrow-up",
                    style={"font-size": "5rem", "color": "mediumseagreen"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-success align-content-center",
)

card01 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("(21) Waste recycling", className="card-title align-middle"),
                html.I(
                    className="bi bi-arrow-right",
                    style={"font-size": "5rem", "color": "orange"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-success",
)

card02 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5(
                    "(22) North East Mining and Groundwater Constraints Map",
                    className="card-title",
                ),
                html.I(
                    className="bi bi-arrow-up",
                    style={"font-size": "5rem", "color": "mediumseagreen"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-success",
)

economic_circular_summary = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("", className="card-title py-3 text-center"),
                dbc.Button(
                    "Explore indicators",
                    href="/economic_circular",
                    color="primary",
                    className="py-3 col-12 mx-auto",
                ),
            ]
        )
    ],
    outline=True,
    className="border-success",
)

cardrow1 = dbc.CardGroup(
    [card00, card01, card02, economic_circular_summary], className="mb-4"
)


#### Row 2: Energy
economic_energy = dbc.CardGroup(
    dbc.Card(
        [dbc.CardBody(html.H4(children="Energy"))],
        outline=True,
        className="py-2 border-warning",
    ),
    className="mb-2",
)

card03 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5(
                    "(24) Regional renewable ; sites, capacity, generation, GVA",
                    className="card-title",
                ),
                html.I(
                    className="bi bi-arrow-up",
                    style={"font-size": "5rem", "color": "mediumseagreen"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-warning",
)

card04 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5(
                    "(25) Regional consumption of gas, electric, road transport and residual fuel",
                    className="card-title",
                ),
                html.I(
                    className="bi bi-arrow-right",
                    style={"font-size": "5rem", "color": "orange"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-warning",
)

card05 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5(
                    "(26) Regional energy consumption: electric and gas – and by sector",
                    className="card-title",
                ),
                html.I(
                    className="bi bi-arrow-right",
                    style={"font-size": "5rem", "color": "mediumseagreen"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-warning",
)

card06 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("(27) Community Energy", className="card-title"),
                html.I(
                    className="bi bi-arrow-right",
                    style={"font-size": "5rem", "color": "mediumseagreen"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-warning",
)

economic_energy_summary = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("Energy", className="card-title py-3 text-center"),
                dbc.Button(
                    "Explore indicators",
                    href="/economic_energy",
                    color="primary",
                    className="py-3 col-12 mx-auto",
                ),
            ]
        )
    ],
    outline=True,
    className="border-warning",
)

cardrow2 = dbc.CardGroup(
    [card03, card04, card05, card06, economic_energy_summary], className="mb-4"
)

economic_also = dbc.CardGroup(
    dbc.Card(
        [dbc.CardBody(html.H4(children="And also"))],
        outline=True,
        className="py-2 border-info",
    ),
    className="mb-2",
)

card07 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("(29) NEPO – public sector spend", className="card-title"),
                html.I(
                    className="bi bi-arrow-up",
                    style={"font-size": "5rem", "color": "red"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-info",
)

card08 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("(30) TVCA and NELEP evidence hubs", className="card-title"),
                html.I(
                    className="bi bi-arrow-up",
                    style={"font-size": "5rem", "color": "mediumseagreen"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-info",
)

card09 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5(
                    "(31) Resources energy analysis programme (scandanavia)",
                    className="card-title",
                ),
                html.I(
                    className="bi bi-arrow-down",
                    style={"font-size": "5rem", "color": "red"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-info",
)

card10 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("(32) Data re ports in region", className="card-title"),
                html.I(
                    className="bi bi-arrow-down",
                    style={"font-size": "5rem", "color": "red"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-info",
)

economic_also_summary = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("And also", className="card-title py-3 text-center"),
                dbc.Button(
                    "Explore indicators",
                    href="/economic_also",
                    color="primary",
                    className="py-3 col-12 mx-auto",
                ),
            ]
        )
    ],
    outline=True,
    className="border-info",
)

cardrow3 = dbc.CardGroup([card07, card08, card09, card10], className="mb-4")

layout = dbc.Container(
    [
        dbc.Row(dbc.Col(html.H1(children="Economic Capital"), className="py-3")),
        dbc.Row(
            dbc.Col(
                html.H4(
                    children="Contribution of our economy to greening the North East of England"
                ),
                className="mb-2",
            )
        ),
        dbc.Row(
            dbc.Col(
                html.P(
                    children="The transition to a green economy is the focus of this metric. Tracking the growth in green training and employment opportunities, reporting on the change in carbon intensity of the economy and transport use and how the economic sector is reducing its environmental impact."
                ),
                className="mb-4",
            ),
        ),
        dbc.Row(economic_circular),
        dbc.Row(cardrow1),
        dbc.Row(economic_energy),
        dbc.Row(cardrow2),
        dbc.Row(economic_also),
        dbc.Row(cardrow3),
    ]
)
