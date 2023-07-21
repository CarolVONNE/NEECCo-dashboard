import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app, neecco_palette

## import data loader helper
from locations_loader import LocationsLoader

# initialise locations loader
locations = LocationsLoader()


# Sections

# Section 1: page title
title = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H1("Just Transition: And Also ", className="py-3")])]),
        html.P(
            "Without any consensus on the idea of a just transition, a wide range of starting points seem useful."
        ),
    ],
    class_name="container-type1",
)


# Section 2: content
content = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.A(
                            [
                                html.Img(
                                    src=locations.get_link("just_transition_ILO"),
                                    width="100%",
                                    title="Click on the screenshot to go to the website",
                                )
                            ],
                            href="https://www.ilo.org/global/topics/green-jobs/publications/WCMS_432859/lang--en/index.htm",
                            target="_blank",
                        ),
                        html.A(
                            "Source: International Labour Organization",
                            href="https://www.ilo.org/global/topics/green-jobs/publications/WCMS_432859/lang--en/index.htm",
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
                        html.A(
                            [
                                html.Img(
                                    src=locations.get_link("just_transition_EU"),
                                    width="100%",
                                    title="Click on the screenshot to go to the website",
                                )
                            ],
                            href="https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/european-green-deal/finance-and-green-deal/just-transition-mechanism_en",
                            target="_blank",
                        ),
                        html.A(
                            "Source: The Just Transition Mechanism (europa.eu)",
                            href="https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/european-green-deal/finance-and-green-deal/just-transition-mechanism_en",
                            target="_blank",
                        ),
                    ],
                    xs=12,
                    sm=12,
                    md=12,
                    lg=6,
                    xl=6,
                ),
            ],
            style={"padding-bottom": "30px"},
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.A(
                            [
                                html.Img(
                                    src=locations.get_link("just_transition_CEN"),
                                    width="100%",
                                    title="Click on the screenshot to go to the website",
                                )
                            ],
                            href="https://www.cen.uk.com/north-sea-transition",
                            target="_blank",
                        ),
                        html.A(
                            "Source: North Sea transition | Conservative Environment Network (cen.uk.com)",
                            href="https://www.cen.uk.com/north-sea-transition",
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
                        html.A(
                            [
                                html.Img(
                                    src=locations.get_link("just_transition_IPPR"),
                                    width="100%",
                                    title="Click on the screenshot to go to the website",
                                )
                            ],
                            href="https://www.ippr.org/research/publications/net-zero-places",
                            target="_blank",
                        ),
                        html.A(
                            "Source: The Progressive Policy Think Tank (IPPR)",
                            href="https://www.ippr.org/research/publications/net-zero-places",
                            target="_blank",
                        ),
                    ],
                    xs=12,
                    sm=12,
                    md=12,
                    lg=6,
                    xl=6,
                ),
            ],
            style={"padding-bottom": "30px"},
        ),
    ],
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
                        content,
                    ]
                )
            ]
        )
    ]
)
