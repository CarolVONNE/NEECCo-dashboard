import plotly.graph_objects as go
import pandas as pd

import dash
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

#### Row 1: Our Communities
social_communities = dbc.CardGroup(
    dbc.Card(
        [dbc.CardBody(html.H4(children="Our Communities"))],
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
                    "Huge amount of [not directly green connected] SE data on this dashboard",
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
                html.H5(
                    "Household disposable income", className="card-title align-middle"
                ),
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
                html.H5("Financial hardship comparisons", className="card-title"),
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

card03 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("Health inequalities", className="card-title"),
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

social_communities_summary = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("Our communities", className="card-title py-3 text-center"),
                dbc.Button(
                    "Explore indicators",
                    href="/social_communities",
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
    [card00, card01, card02, card03, social_communities_summary], className="mb-4"
)


#### Row 2: Engagement with Nature
social_nature = dbc.CardGroup(
    dbc.Card(
        [dbc.CardBody(html.H4(children="Engagement with nature"))],
        outline=True,
        className="py-2 border-warning",
    ),
    className="mb-2",
)

card04 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5(
                    "Number of hours volunteering around conservation",
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

card05 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("Community life survey", className="card-title"),
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

card06 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5(
                    "Monitor of engagement with the natural envrionment and then the people and nature survey",
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

card07 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5(
                    "Key regional grant funders distribution", className="card-title"
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

social_nature_summary = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5(
                    "Green Jobs and Research", className="card-title py-3 text-center"
                ),
                dbc.Button(
                    "Explore indicators",
                    href="/social_nature",
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
    [card04, card05, card06, card07, social_nature_summary], className="mb-4"
)


#### Row 3: and also
social_also = dbc.CardGroup(
    dbc.Card(
        [dbc.CardBody(html.H4(children="And also"))],
        outline=True,
        className="py-2 border-info",
    ),
    className="mb-2",
)

card08 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5(
                    'Climate friendly schools and eco-schools, className="card-title'
                ),
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

card09 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5(
                    "Active travel: walking and cycle infrastructure",
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
    className="border-info",
)

card10 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("Distance travelled by mode", className="card-title"),
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

social_also_summary = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5(
                    "Reducing Environmental Impact",
                    className="card-title py-3 text-center",
                ),
                dbc.Button(
                    "Explore indicators",
                    href="/economic_environmental",
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
    [card08, card09, card10, social_also_summary], className="mb-4"
)


layout = dbc.Container(
    [
        dbc.Row(dbc.Col(html.H1(children="Social Capital"), className="py-3")),
        dbc.Row(
            dbc.Col(
                html.H4(
                    children="How are we achieving a sustainable future for our communities?"
                ),
                className="mb-2",
            )
        ),
        dbc.Row(
            dbc.Col(
                html.P(
                    children="The climate crisis and ecological collapse are a result of human activity. They are and will increasingly affect our health and wellbeing. We need to change our behaviours and relationships with the natural world individually and collectively. Over time this set of metrics will indicate the impact of the climate crisis and if we are making sufficient changes."
                ),
                className="mb-4",
            ),
        ),
        dbc.Row(social_communities),
        dbc.Row(cardrow1),
        dbc.Row(social_nature),
        dbc.Row(cardrow2),
        dbc.Row(social_also),
        dbc.Row(cardrow3),
    ]
)
