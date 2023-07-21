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
    locations.get_link("social_nature_third_sector_trends_impact_on_local_env"),
    delimiter=",",
    header=0,
    usecols=[0, 1],
)

df2 = pd.read_csv(
    locations.get_link("social_nature_funders"), delimiter=",", header=0, usecols=[0]
)

# create figures
fig1 = px.histogram(df1, x="region", y="percentage", template="simple_white")
fig1.update_traces(marker_color=neecco_palette[0])
fig1.update_layout(yaxis=dict(title="percentage"))


# Sections

# Section 1: page title
title = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("Social: Engagement With Nature", className="py-3"),
                        html.P(
                            [
                                "Between 2009 and 2919 national research was undertaken with reporting on a regional level being available. The ‘monitoring engagement in natural environment survey’ has since been replaced by the ‘people and nature survey’. (",
                                html.Span(
                                    [
                                        html.A(
                                            "Welcome to the People and Nature Survey (arcgis.com)",
                                            href="https://people-and-nature-survey-defra.hub.arcgis.com/",
                                        )
                                    ]
                                ),
                                ") The results of this are not currently available on a regional basis.",
                            ]
                        ),
                        html.P(
                            [
                                "While there are many voluntary and community organisations that focus on the environment, for most it is not a focus of their work. The Third Sector Trends survey was started in the region – a huge range of research can be found at ",
                                html.Span(
                                    [
                                        html.A(
                                            "https://www.communityfoundation.org.uk/our-resources/?listing-category=third-sector-trends",
                                            href="https://www.communityfoundation.org.uk/our-resources/?listing-category=third-sector-trends",
                                        )
                                    ]
                                ),
                                ".",
                            ]
                        ),
                        html.P(
                            "Charitable Foundations have a key role to play in enabling voluntary organisations to address their impact on the climate and nature, as well as integrating and responding to these issues as part of their day job."
                        ),
                    ]
                )
            ]
        ),
        dbc.Row(
            dbc.Col(
                [
                    html.H4("Page content"),
                    html.Ul(
                        [
                            html.Li(
                                html.A(html.P("Engaging with Nature"), href="#section1")
                            ),
                            html.Li(
                                html.A(
                                    html.P(
                                        "Third sector organisations contribution to the environment"
                                    ),
                                    href="#section2",
                                )
                            ),
                            html.Li(
                                html.A(
                                    html.P("Key regional grant funders"),
                                    href="#section3",
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

# Section: Monitoring of engagement with the natural environment
monitor_of_engagement = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Engaging with Nature"),
                        html.P(
                            [
                                "The Monitoring Engagement in the Natural Environment Survey (2009 - 2019) dashboard was developed by ",
                                html.A(
                                    "Natural England",
                                    href="https://www.gov.uk/government/organisations/natural-england",
                                    target="_blank",
                                ),
                                ". The dashboard contains a section on environmental attitudes by region. Click on the image below to visit the dashboard and explore the results of the Natural England survey.",
                            ]
                        ),
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
                                    src=locations.get_link(
                                        "monitoring_engagement_in_the_natural_environment_survey"
                                    ),
                                    width="100%",
                                    alt="A screenshot of the Natural England Monitoring Engagement in the Natural Environment Survey (2009 - 2019) dashboard",
                                    title="Click on the image to visit the Natural England dashboard",
                                )
                            ],
                            href="https://defra.maps.arcgis.com/apps/MapSeries/index.html?appid=2f24d6c942d44e81821c3ed2d4ab2ada",
                            target="_blank",
                        ),
                    ],
                    xs=12,
                    sm=12,
                    md=12,
                    lg=8,
                    xl=8,
                ),
                dbc.Col(
                    [
                        html.Ul(
                            [
                                html.Li(
                                    html.P(
                                        [
                                            "A dashboard by Natural England: ",
                                            html.A(
                                                "Monitoring engagement in the natural environment survery (2009-2019)",
                                                href="https://defra.maps.arcgis.com/apps/MapSeries/index.html?appid=2f24d6c942d44e81821c3ed2d4ab2ada",
                                                target="_blank",
                                            ),
                                        ]
                                    )
                                ),
                                html.Li(
                                    html.P(
                                        [
                                            "Additional resource: ",
                                            html.A(
                                                "The People and Nature User Hub",
                                                href="https://people-and-nature-survey-defra.hub.arcgis.com",
                                                target="_blank",
                                            ),
                                        ]
                                    )
                                ),
                            ]
                        ),
                    ],
                    xs=12,
                    sm=12,
                    md=12,
                    lg=4,
                    xl=4,
                ),
            ]
        ),
    ],
    id="section1",
    class_name="container-type1",
)


# Section: Third sector organisations contribution to the environment
conservation_volunteers = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2(
                            "Third sector organisations contribution to the environment"
                        ),
                        html.H5(
                            "The percentage of third sector organisations that say they have a very strong impact on or make a good contribution to the local environment in 2022"
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
                            [
                                "Third Sector Trends Study, Professor Tony Chapman, Durham University, funded by the Community Foundation. For more information see : ",
                                html.Span(
                                    [
                                        html.A(
                                            "https://www.communityfoundation.org.uk/our-resources/?listing-category=third-sector-trends",
                                            href="https://www.communityfoundation.org.uk/our-resources/?listing-category=third-sector-trends",
                                        )
                                    ]
                                ),
                            ]
                        ),
                        html.A(
                            "Data Source: The Community Foundation Tyne & Wear and Northumberland Annual Third Sector Trends Survey",
                            href="https://www.communityfoundation.org.uk/third-sector-trends/",
                            target="_blank",
                        ),
                    ],
                    align="centre",
                )
            ]
        )
    ],
    id="section2",
    class_name="container-type1",
)

# Section: Key regional grant funders
grant_funders = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Key regional grant funders"),
                    ]
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H5(
                            "All the funders in the FINE (Funding Information North East) directory in November 2022, that state they fund environmental work."
                        ),
                        html.H5("Scroll to view all funders."),
                        dash_table.DataTable(
                            df2.to_dict("records"),
                            [{"name": i, "id": i} for i in df2.columns],
                            style_table={"height": "300px", "overflowY": "auto"},
                            style_cell={"textAlign": "left"},
                            style_header={
                                "backgroundColor": "#669900",
                                "color": "white",
                                "font-weight": "bold",
                            },
                            id="tbl",
                        ),
                    ],
                    xs=12,
                    sm=12,
                    md=12,
                    lg=9,
                    xl=9,
                ),
                dbc.Col(
                    [
                        html.A(
                            "Data Source: Funding Information North East (FINE) directory",
                            href="https://www.vonne.org.uk/funding",
                            target="_blank",
                        )
                    ],
                    xs=12,
                    sm=12,
                    md=12,
                    lg=3,
                    xl=3,
                ),
                html.Br(),
            ]
        ),
    ],
    id="section3",
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
                        monitor_of_engagement,
                        conservation_volunteers,
                        grant_funders,
                    ]
                )
            ]
        )
    ]
)
