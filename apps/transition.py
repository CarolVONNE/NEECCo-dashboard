import plotly.graph_objects as go
import pandas as pd

import dash
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

### Row 1: At home
transition_home = dbc.CardGroup(
    dbc.Card(
        [dbc.CardBody(html.H4(children="At home"))],
        outline=True,
        className="py-2 border-success",
    ),
    className="mb-2",
)

card00 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("Fuel poverty", className="card-title"),
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
                html.H5("Housing efficiency", className="card-title align-middle"),
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
                html.H5("Food", className="card-title"),
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

transition_home_summary = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("At home", className="card-title py-3 text-center"),
                dbc.Button(
                    "Explore indicators",
                    href="/transition_home",
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
    [card00, card01, card02, transition_home_summary], className="mb-4"
)


#### Row 2: At work
transition_work = dbc.CardGroup(
    dbc.Card(
        [dbc.CardBody(html.H4(children="At work"))],
        outline=True,
        className="py-2 border-warning",
    ),
    className="mb-2",
)

card03 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("Green economy", className="card-title"),
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
                html.H5("Gender pay gap", className="card-title"),
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
                html.H5("Climate emergency declarations", className="card-title"),
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
                html.H5("Jobs and training", className="card-title"),
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

transition_work_summary = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("At work", className="card-title py-3 text-center"),
                dbc.Button(
                    "Explore indicators",
                    href="/natural_water",
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
    [card03, card04, card05, card06, transition_work_summary], className="mb-4"
)


#### Row 3: And also
transition_also = dbc.CardGroup(
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
                html.H5("Flood risk", className="card-title"),
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
                html.H5("Free school meals", className="card-title"),
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
                html.H5("Environmental protection expenditure", className="card-title"),
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

transition_also_summary = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("And also", className="card-title py-3 text-center"),
                dbc.Button(
                    "Explore indicators",
                    href="/transition_also",
                    color="primary",
                    className="py-3 col-12 mx-auto",
                ),
            ]
        )
    ],
    outline=True,
    className="border-info",
)

cardrow3 = dbc.CardGroup(
    [card07, card08, card09, transition_also_summary], className="mb-4"
)


layout = dbc.Container(
    [
        dbc.Row(dbc.Col(html.H1(children="Just transition"), className="py-3")),
        dbc.Row(
            dbc.Col(
                html.H4(
                    children="Shows the growth in the quality and value of our natural environment"
                ),
                className="mb-2",
            )
        ),
        dbc.Row(
            dbc.Col(
                html.P(
                    children="In theory we could address the climate crisis and ecological breakdown without recognising and rebalancing the deep structural inequalities in our society. In practice, not only would this be morally indefensible it was also be an ineffective and short term response. This set of indicators is a sense check on the traditional triple bottom line of environmental social and economic."
                ),
                className="mb-4",
            ),
        ),
        dbc.Row(transition_home),
        dbc.Row(cardrow1),
        dbc.Row(transition_work),
        dbc.Row(cardrow2),
        dbc.Row(transition_also),
        dbc.Row(cardrow3),
    ]
)
