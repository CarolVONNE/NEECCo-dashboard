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
trips = pd.read_csv(locations.get_link("social_also_trips"))
active_travel = pd.read_csv(locations.get_link("social_also_active_travel"))

# create figures

fig_trips_by_mode = px.line(
    trips,
    x="Year",
    y="Trips per person per year",
    color="Mode",
    markers=False,
    template="simple_white",
    color_discrete_sequence=neecco_palette,
)
fig_active_travel = px.line(
    active_travel,
    x="Year",
    y="Percentage of adults",
    color="Frequency",
    line_dash="Area name",
    markers=True,
    template="simple_white",
    color_discrete_sequence=neecco_palette,
    line_dash_sequence=["dot", "solid"],
)

# Sections

# Section 1: page title
title = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H1("Social: And Also", className="py-3")])]),
        dbc.Row(
            [
                html.P(
                    "Our children and grandchildren will live with the consequences of climate change. Their ability to respond will be significantly influenced by their time at school. There is data from two schemes: a new regionally based initiative and a more established national programme. "
                ),
                html.P(
                    "The focus of this dashboard is the future. This includes a future for our cultural heritage. Our heritage is at risk from many factors with the impact of climate change being increasingly understood. The National Trust owns and manages sites across our region and has led some important work around what they describe as “climate hazards”. "
                ),
                html.P(
                    "Transport is generally understood as an area where change is essential. While the wide ownership of private cars may have increased our sense of independence, the unintended consequences of petrol-powered engines demonstrates our interdependence. One part of the solution is often labelled ‘active travel’. That means walking or cycling for short trips whenever possible. "
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
                                    html.P("Climate friendly schools and eco-schools"),
                                    href="#section1",
                                )
                            ),
                            html.Li(html.A(html.P("Our heritage"), href="#section2")),
                            html.Li(
                                html.A(
                                    html.P("Number of trips by mode"), href="#section3"
                                )
                            ),
                            html.Li(
                                html.A(html.P("Walking and cycling"), href="#section4")
                            ),
                        ]
                    ),
                ]
            ),
        ),
    ],
    class_name="container-type1",
)

# Section 3: Climate friendly schools and eco-Schools
schools = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Climate friendly schools and eco-schools"),
                        html.P(
                            html.A(
                                "Climate Friendly Schools",
                                href="https://www.climatefriendlyschools.org.uk/",
                                target="_blank",
                            )
                        ),
                        html.H3("Eco-Schools North East statistics"),
                        html.P(
                            html.A(
                                "Eco-Schools",
                                href="https://www.eco-schools.org.uk/",
                                target="_blank",
                            )
                        ),
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            "622 NE schools",
                            style={
                                "background-color": "#669900",
                                "font-weight": "bold",
                                "color": "white",
                                "text-align": "center",
                                "padding": "10px 0px 10px 0px",
                            },
                        ),
                        html.P(
                            "The number of NE schools registered with the Eco-Schools programme and have been active in the last 5 years."
                        ),
                    ],
                    xs=12,
                    sm=12,
                    md=6,
                    lg=3,
                    xl=3,
                ),
                dbc.Col(
                    [
                        html.P(
                            "17,625kg",
                            style={
                                "background-color": "#669900",
                                "font-weight": "bold",
                                "color": "white",
                                "text-align": "center",
                                "padding": "10px 0px 10px 0px",
                            },
                        ),
                        html.P(
                            "The amount of waste diverted from landfill in 2021-22 by schools in the NE as part of the Eco-School programme"
                        ),
                    ],
                    xs=12,
                    sm=12,
                    md=6,
                    lg=3,
                    xl=3,
                ),
                dbc.Col(
                    [
                        html.P(
                            "5,477 young people",
                            style={
                                "background-color": "#669900",
                                "font-weight": "bold",
                                "color": "white",
                                "text-align": "center",
                                "padding": "10px 0px 10px 0px",
                            },
                        ),
                        html.P(
                            "The number of young people who delivered a litter pick in 2021-22 as part of their Eco-School activities"
                        ),
                    ],
                    xs=12,
                    sm=12,
                    md=6,
                    lg=3,
                    xl=3,
                ),
                dbc.Col(
                    [
                        html.P(
                            "5,487 young people",
                            style={
                                "background-color": "#669900",
                                "font-weight": "bold",
                                "color": "white",
                                "text-align": "center",
                                "padding": "10px 0px 10px 0px",
                            },
                        ),
                        html.P(
                            "The number of young people who benefitted from increased plant based options on their schools dinner menu as a result of their school working on the Eco-schools programme in 2021-22."
                        ),
                    ],
                    xs=12,
                    sm=12,
                    md=6,
                    lg=3,
                    xl=3,
                ),
            ]
        ),
    ],
    id="section1",
    class_name="container-type1",
)

# Section 6: Our heritage
our_heritage = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Our heritage"),
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3("Historic England - Heritage at Risk"),
                        html.A(
                            [
                                html.Img(
                                    src=locations.get_link(
                                        "social_also_historic_england"
                                    ),
                                    width="100%",
                                )
                            ],
                            href="https://experience.arcgis.com/experience/cb50293b60cd42e98f7d312cec9115a9/",
                            target="_blank",
                        ),
                        html.P(
                            html.A(
                                "Historic England - Heritage at Risk map",
                                href="https://experience.arcgis.com/experience/cb50293b60cd42e98f7d312cec9115a9/",
                                target="_blank",
                            )
                        ),
                        html.P(
                            html.A(
                                "Historic England - Heritage at Risk Register 2022, North East and Yorkshire (pdf)",
                                href="https://historicengland.org.uk/images-books/publications/har-2022-registers/ne-yo-har-register2022/",
                                target="_blank",
                            )
                        ),
                        html.P(
                            html.A(
                                "Historic England - Research Issue 19 (pdf)",
                                href="https://historicengland.org.uk/images-books/publications/historic-england-research-19/he-research-19/",
                                target="_blank",
                            )
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        html.H3("National Trust - Climate Hazards"),
                        html.A(
                            [
                                html.Img(
                                    src=locations.get_link(
                                        "social_also_national_trust"
                                    ),
                                    width="100%",
                                )
                            ],
                            href="https://national-trust.maps.arcgis.com/apps/webappviewer/index.html?id=a44672bb34c4491a909034d0eed76583",
                            target="_blank",
                        ),
                        html.P(
                            html.A(
                                "National Trust - Climate Hazards map",
                                href="https://national-trust.maps.arcgis.com/apps/webappviewer/index.html?id=a44672bb34c4491a909034d0eed76583",
                                target="_blank",
                            )
                        ),
                        html.P(
                            html.A(
                                "‘A game changer’ – 3Keel and National Trust map climate risks to historic UK sites",
                                href="https://www.3keel.com/climate-risk-mapping/",
                                target="_blank",
                            )
                        ),
                    ]
                ),
            ]
        ),
    ],
    id="section2",
    class_name="container-type1",
)

# Section 5: Distance travelled by mode
trips_by_mode = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H2("Number of trips by mode")])]),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H5("Trips per person per year in the North East"),
                        dcc.Graph(
                            id="grph1",
                            figure=fig_trips_by_mode,
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
                            href="https://www.gov.uk/government/statistical-data-sets/nts03-modal-comparisons",
                            target="_blank",
                        ),
                        html.P(
                            [
                                "See also: ",
                                html.A(
                                    "Impact of Covid19 - Main findings from the National Travel Survey 2021",
                                    href="https://www.gov.uk/government/statistics/national-travel-survey-2021/national-travel-survey-2021-introduction-and-main-findings#main-findings",
                                    target="_blank",
                                ),
                            ]
                        ),
                    ]
                )
            ]
        ),
    ],
    id="section3",
    class_name="container-type1",
)


# Section 5: Walking and cycling
walking_and_cycling = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col([html.H2("Walking and cycling")]),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H5("Proportion of adults who walk or cycle regularly"),
                        dcc.Graph(
                            id="grph2",
                            figure=fig_active_travel,
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
                            href="https://www.gov.uk/government/statistical-data-sets/walking-and-cycling-statistics-cw",
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
                    [title, schools, our_heritage, trips_by_mode, walking_and_cycling]
                )
            ]
        )
    ]
)
