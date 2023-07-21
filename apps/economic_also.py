import plotly.graph_objects as go
import pandas as pd

import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

from app import app, neecco_palette

from locations_loader import LocationsLoader


# initialise locations loader
locations = LocationsLoader()

# Sections

# Section 1: page title
title = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H1("Economic: And Also", className="py-3")])]),
        dbc.Row(
            [
                html.P(
                    "During recent years the region has had two public sector organisations with a focus on economic growth: Tees Valley Combined Authority and the North East Local Economic Partnership which covers from the Scottish boarder to the south of County Durham.  These two agencies have drawn together much important data and evidence. "
                ),
                html.P(
                    "Climate change and the ecological breakdown are completely independent of human boundaries. Our responses need to be joined up internationally as well as with our neighbouring regions and nation. It is important to note that this international connectivity is not included in the United Nations Climate CoP targets. "
                ),
            ]
        ),
        dbc.Row(
            dbc.Col(
                [
                    html.H4("Page content"),
                    html.Ul(
                        [
                            html.Li(
                                html.A(
                                    html.P("TVCA and NELEP evidence hubs"),
                                    href="#section1",
                                )
                            ),
                            html.Li(
                                html.A(
                                    html.P("International connectivity"),
                                    href="#section2",
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


# Section 2: TVCA and NELEP evidence hubs
evidence_hubs = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col([html.H2("TVCA and NELEP evidence hubs")]),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P("Placeholder for some text/context."),
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.A(
                            [
                                html.Img(
                                    src=locations.get_link("economic_also_neeh"),
                                    width="100%",
                                )
                            ],
                            href="https://evidencehub.northeastlep.co.uk/transition-to-net-zero",
                            target="_blank",
                        ),
                        html.A(
                            [
                                html.P(
                                    "North East Evidence Hub - Transition to Net Zero"
                                )
                            ],
                            href="https://evidencehub.northeastlep.co.uk/transition-to-net-zero",
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
                                    src=locations.get_link(
                                        "economic_also_tv_nz_strategy"
                                    ),
                                    width="100%",
                                )
                            ],
                            href="https://teesvalley-ca.gov.uk/business/wp-content/uploads/sites/3/2023/03/Net-Zero-strategy-Digital.pdf",
                            target="_blank",
                        ),
                        html.A(
                            [
                                html.P(
                                    "Source: Tees Valley Combined Authority: Net Zero"
                                )
                            ],
                            href="https://teesvalley-ca.gov.uk/business/net-zero/",
                            target="_blank",
                        ),
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
    id="section1",
    class_name="container-type1",
)


# Section 2: data re ports in region
international_connectivity = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H2("International connectivity")])]),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.A(
                            [
                                html.Img(
                                    src=locations.get_link(
                                        "economic_also_maritime_statistics"
                                    ),
                                    width="100%",
                                )
                            ],
                            href="https://maps.dft.gov.uk/maritime-statistics/index.html",
                            target="_blank",
                        ),
                        html.A(
                            [html.P("Maritime statistics: interactive dashboard")],
                            href="https://maps.dft.gov.uk/maritime-statistics/index.html",
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
                        html.P("See also - regional airports"),
                        html.A(
                            [html.P("Teeside International Airport")],
                            href="https://www.teessideinternational.com/about-us/",
                            target="_blank",
                        ),
                        html.A(
                            [
                                html.P(
                                    "Newcastle International Airport (Net Zero Carbon 2035)"
                                )
                            ],
                            href="https://www.newcastleairport.com/about-your-airport/environment/net-zero-carbon-2035/",
                            target="_blank",
                        ),
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
    id="section2",
    class_name="container-type1",
)


# create layout
layout = dbc.Container(
    [dbc.Row([dbc.Col([title, evidence_hubs, international_connectivity])])]
)
