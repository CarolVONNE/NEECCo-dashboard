import plotly.graph_objects as go
import pandas as pd
from dash import html, dcc, dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
from app import app, neecco_palette

from locations_loader import LocationsLoader

# initialise locations loader
locations = LocationsLoader()

# read data
df1 = pd.read_csv(
    locations.get_link("carbon_pathway_projections"), delimiter=",", header=0
)

# create figures
fig1 = px.line(
    df1,
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
    # color_discrete_sequence=neecco_palette,
)
fig1.update_layout(
    legend=dict(
        orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, title=""
    )
)
# Sections
# Section 1: Indicator information
indicators = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.P(
                                    [
                                        "To stay under 1.5°C warming, and prevent the worst effects of climate change from becoming irreversible we have:"
                                    ]
                                ),
                                html.Iframe(
                                    srcDoc="<script src='https://climateclock.world/widget-v2.js' async></script><climate-clock />",
                                    style={"width": "100%"},
                                ),
                                html.A(
                                    "Source: climateclock.world",
                                    href="https://climateclock.world",
                                    target="_blank",
                                    style={
                                        "display": "block",
                                        "text-align": "right",
                                        "margin-top": "-30px",
                                    },
                                ),
                            ]
                        ),
                        html.H1(
                            "Indicators for the North East of England",
                            className="py-3",
                        ),
                        html.P("Today we have one less day than yesterday. "),
                        html.P(
                            "This resource brings together some of the most important information about climate change, the ecological collapse and the need for a just transition within the North East of England. Inclusion is based on available material that meets a set of criteria. It is a partial and constantly changing picture. We need information to understand the changes we must make individually and collectively – and the changes that we need others to make within and beyond our region.",
                        ),
                        html.P(
                            [
                                html.B("Please note: "),
                                "On the graphs hover your cursor over the lines for more detail. You can use the icons in the top right hand corner of the graphs to adjust the image.",
                            ]
                        ),
                        html.Div(
                            [
                                dbc.Button(
                                    "Carbon",
                                    href="/carbon",
                                    color="primary",
                                    className="me-1",
                                ),
                            ],
                            className="d-grid gap-2 col-12 mx-auto",
                        ),
                    ]
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2(
                            "Nature",
                            className="py-3",
                        ),
                        html.Div(
                            [
                                dbc.Button(
                                    "Land",
                                    href="/natural_land",
                                    color="primary",
                                    className="me-1",
                                ),
                                dbc.Button(
                                    "Water",
                                    href="/natural_water",
                                    color="primary",
                                    className="me-1",
                                ),
                                dbc.Button(
                                    "And also",
                                    href="/natural_also",
                                    color="primary",
                                    className="me-1",
                                ),
                            ],
                            className="d-grid gap-2 col-12 mx-auto",
                        ),
                        html.Br(),
                        html.P(
                            [
                                "The World Wildlife Fund ",
                                html.Span(
                                    [
                                        html.A(
                                            "https://www.worldwildlife.org/",
                                            href="https://www.worldwildlife.org/",
                                            target="_blank",
                                        )
                                    ]
                                ),
                                ' defines biodiversity as "all the different kinds of life you’ll find in one area—the variety of animals, plants, fungi, and even microorganisms like bacteria that make up our natural world. Each of these species and organisms work together in ecosystems, like an intricate web, to maintain balance and support life. Biodiversity supports everything in nature that we need to survive: food, clean water, medicine, and shelter." ',
                            ]
                        ),
                    ],
                    xs=12,
                    sm=6,
                    md=6,
                    lg=3,
                    xl=3,
                ),
                dbc.Col(
                    [
                        html.H2(
                            "Economic",
                            className="py-3",
                        ),
                        html.Div(
                            [
                                dbc.Button(
                                    "Towards a circular economy",
                                    href="/economic_circular",
                                    color="primary",
                                    className="me-1",
                                ),
                                dbc.Button(
                                    "Energy",
                                    href="/economic_energy",
                                    color="primary",
                                    className="me-1",
                                ),
                                dbc.Button(
                                    "And also",
                                    href="/economic_also",
                                    color="primary",
                                    className="me-1",
                                ),
                            ],
                            className="d-grid gap-2 col-12 mx-auto",
                        ),
                        html.Br(),
                        html.P(
                            "We don’t know what a post-carbon economy will look like: or if it is more useful to think about it as green or sustainable or circular. Clearly there is a significant way to go as the clock ticks down. "
                        ),
                        html.P(
                            "We do have some important starting points with emerging sectors along with a changing energy industry. While we are building our future we cannot ignore the inheritance from our historical production and consumption - and there are also issues of geography. "
                        ),
                    ],
                    xs=12,
                    sm=6,
                    md=6,
                    lg=3,
                    xl=3,
                ),
                dbc.Col(
                    [
                        html.H2(
                            "Social",
                            className="py-3",
                        ),
                        html.Div(
                            [
                                dbc.Button(
                                    "Our communities",
                                    href="/social_communities",
                                    color="primary",
                                    className="me-1",
                                ),
                                dbc.Button(
                                    "Engagement with nature",
                                    href="/social_nature",
                                    color="primary",
                                    className="me-1",
                                ),
                                dbc.Button(
                                    "And also",
                                    href="/social_also",
                                    color="primary",
                                    className="me-1",
                                ),
                            ],
                            className="d-grid gap-2 col-12 mx-auto",
                        ),
                        html.Br(),
                        html.P(
                            "The climate crisis and ecological collapse are the result of human activity. They are increasingly affecting our health and wellbeing.",
                        ),
                        html.P(
                            'We need to move to a model of sustainable development. This is usually defined as "development that meets the needs of the present without compromising the ability of future generations to meet their own needs." (‘Our Common Future’, 1987) '
                        ),
                        html.P(
                            "The natural world is not constrained by human boundaries, so we are all in this together."
                        ),
                    ],
                    xs=12,
                    sm=6,
                    md=6,
                    lg=3,
                    xl=3,
                ),
                dbc.Col(
                    [
                        html.H2(
                            "Just Transition",
                            className="py-3",
                        ),
                        html.Div(
                            [
                                dbc.Button(
                                    "At home",
                                    href="/transition_home",
                                    color="primary",
                                    className="me-1",
                                ),
                                dbc.Button(
                                    "At work",
                                    href="/transition_work",
                                    color="primary",
                                    className="me-1",
                                ),
                                dbc.Button(
                                    "And also",
                                    href="/transition_also",
                                    color="primary",
                                    className="me-1",
                                ),
                            ],
                            className="d-grid gap-2 col-12 mx-auto",
                        ),
                        html.Br(),
                        html.P(
                            "There is much debate – and little agreement – over what a ‘just transition’ would be and how it could happen."
                        ),
                        html.P(
                            "Some people we must ensure the transition to a post-carbon economy addresses the deep structural inequalities in our society. In doing this we can draw on the lessons of our region’s transition to a post-industrial society at the end of 20th century."
                        ),
                        html.P(
                            "For others the idea is irrelevant. They believe we can address the climate crisis and ecological breakdown without considering social structures."
                        ),
                    ],
                    xs=12,
                    sm=6,
                    md=6,
                    lg=3,
                    xl=3,
                ),
            ]
        ),
    ],
    class_name="container-type1",
)

# Section 2: Carbon Budget
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
                                "Data Source: Tyndall Centre for Climate Change Research",
                                href="https://carbonbudget.manchester.ac.uk/reports/NE/",
                                target="_blank",
                            )
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
    class_name="container-type1",
)

# create layout
layout = dbc.Container(
    [
        dbc.Row([dbc.Col([indicators])]),
    ]
)
