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

# data
ft_age = pd.read_csv(locations.get_link("transition_work_paygap_ft_age"))
pt_age = pd.read_csv(locations.get_link("transition_work_paygap_pt_age"))
ft_sector = pd.read_csv(locations.get_link("transition_work_paygap_ft_sector"))
pt_sector = pd.read_csv(locations.get_link("transition_work_paygap_pt_sector"))

# create figures
fig_ft_age = px.bar(
    ft_age,
    y="Age",
    x="Median pay gap",
    color="Region",
    barmode="group",
    height=400,
    color_discrete_sequence=neecco_palette,
    template="simple_white",
    orientation="h",
)
fig_pt_age = px.bar(
    pt_age,
    y="Age",
    x="Median pay gap",
    color="Region",
    barmode="group",
    height=400,
    color_discrete_sequence=neecco_palette,
    template="simple_white",
    orientation="h",
)
fig_ft_sector = px.bar(
    ft_sector,
    y="Sector",
    x="Median pay gap",
    color="Region",
    barmode="group",
    height=400,
    color_discrete_sequence=neecco_palette,
    template="simple_white",
    orientation="h",
)
fig_pt_sector = px.bar(
    pt_sector,
    y="Sector",
    x="Median pay gap",
    color="Region",
    barmode="group",
    height=400,
    color_discrete_sequence=neecco_palette,
    template="simple_white",
    orientation="h",
)

# Sections

# Section 1: page title
title = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H1("Just Transition: At Work", className="py-3")])]),
        dbc.Row(
            dbc.Col(
                [
                    html.H4("Page content"),
                    html.Ul(
                        [
                            html.Li(
                                html.A(
                                    html.P("Opportunities in the green economy"),
                                    href="#section1",
                                )
                            ),
                            html.Li(html.A(html.P("Gender pay gap"), href="#section2")),
                            html.Li(
                                html.A(
                                    html.P("Councils declaring a climate emergency"),
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

# Section 3: Green economy opportunities: big projects
big_projects = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Opportunities in the green economy"),
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            [
                                "As our economy becomes greener, the nature of many jobs will change. The ",
                                html.Span(
                                    [
                                        html.A(
                                            "Labour Market Profile",
                                            href="https://www.nomisweb.co.uk/reports/lmp/gor/2013265921/report.aspx",
                                        )
                                    ]
                                ),
                                " brings together data from several sources to show where we are now. There is ",
                                html.Span(
                                    [
                                        html.A(
                                            "national",
                                            href="https://eciu.net/analysis/reports/2023/mapping-the-uk-net-zero-economy",
                                        )
                                    ]
                                ),
                                " and ",
                                html.Span(
                                    [
                                        html.A(
                                            "regional",
                                            href="https://www.gov.uk/government/publications/net-zero-in-the-north-east-of-england-regional-transition-impacts",
                                        )
                                    ]
                                ),
                                " research that gives more forward-focused pictures, with initiatives such as our region’s Off-Shore Wind Cluster exemplifying the opportunities.",
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
                                        "transition_work_energy_coast"
                                    ),
                                    width="100%",
                                    alt="A map of the North East England Energi Coast",
                                    title="Click on the image to visit Energi Coast information about Offshore Wind in North East England",
                                )
                            ],
                            href="https://energicoast.co.uk/about/about-offshore-wind-in-north-east-england/",
                            target="_blank",
                        ),
                        html.P(
                            html.A(
                                "Energi coast",
                                href="http://www.energicoast.co.uk/",
                                target="_blank",
                            )
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
                        html.P(
                            html.A(
                                "Labour Market Profile: North East",
                                href="https://www.nomisweb.co.uk/reports/lmp/gor/2013265921/report.aspx",
                                target="_blank",
                            )
                        ),
                        html.P(
                            html.A(
                                "Mapping the Net Zero economy",
                                href="https://eciu.net/analysis/reports/2023/mapping-the-uk-net-zero-economy",
                                target="_blank",
                            )
                        ),
                        html.P(
                            html.A(
                                "Net Zero in the North East of England",
                                href="https://www.gov.uk/government/publications/net-zero-in-the-north-east-of-england-regional-transition-impacts",
                                target="_blank",
                            )
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


# Section 4: Gender pay gap
gender_pay_gap = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Gender pay gap"),
                        html.P(
                            "The Equal Pay Act became law in 1970. The graphs below compare the most recent regional and UK-wide data. A prize is offered for any better illustration of the ‘policy-implementation’ gap!  "
                        ),
                    ]
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H5("Gender pay gap for full-time workers by age, 2022"),
                        dcc.Graph(
                            id="grph3",
                            figure=fig_ft_age,
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
                            "Data Source: ONS",
                            href="https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/datasets/annualsurveyofhoursandearningsashegenderpaygaptables",
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
                        html.H5("Gender pay gap for part-time workers by age, 2022"),
                        dcc.Graph(
                            id="grph3",
                            figure=fig_pt_age,
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
                            "Data Source: ONS",
                            href="https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/datasets/annualsurveyofhoursandearningsashegenderpaygaptables",
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
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H5("Gender pay gap for full-time workers by sector, 2022"),
                        dcc.Graph(
                            id="grph3",
                            figure=fig_ft_sector,
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
                            "Data Source: ONS",
                            href="https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/datasets/annualsurveyofhoursandearningsashegenderpaygaptables",
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
                        html.H5("Gender pay gap for part-time workers by sector, 2022"),
                        dcc.Graph(
                            id="grph3",
                            figure=fig_pt_sector,
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
                            "Data Source: ONS",
                            href="https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/datasets/annualsurveyofhoursandearningsashegenderpaygaptables",
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
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            [
                                "Gender pay gap (GPG) - calculated as the difference between average hourly earnings (excluding overtime) of men and women as a proportion of average hourly earnings (excluding overtime) of men. ",
                                "For example, a 4% GPG denotes that women earn 4% less, on average, than men. Conversely, a -4% GPG denotes that women earn 4% more, on average, than men. ",
                                "The median is the middle value in a sorted list of numbers.",
                            ]
                        )
                    ]
                ),
            ]
        ),
    ],
    id="section2",
    class_name="container-type1",
)


# Section 5: Councils declaring a climate emergency
climate_emerg_decs = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Councils declaring a climate emergency"),
                        html.P(
                            [
                                "Our democratically elected bodies have a key leadership role, from Parish Councils see (",
                                html.Span(
                                    [
                                        html.A(
                                            "https://www.nalc.gov.uk/our-work/climate-change",
                                            href="https://www.nalc.gov.uk/our-work/climate-change",
                                        )
                                    ]
                                ),
                                ") up.",
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
                        html.H5("CAPE database"),
                        html.P(
                            [
                                html.A(
                                    "CAPE",
                                    href="https://cape.mysociety.org/",
                                    target="_blank",
                                ),
                                " is a fully searchable database of UK local authority climate action plans, climate targets, and climate emergency declarations. Click the image below to visit the CAPE database and search for a local authority.",
                            ]
                        ),
                        html.A(
                            [
                                html.Img(
                                    src=locations.get_link("transition_work_cape"),
                                    width="100%",
                                    alt="Click the image to view the CAPE database of climate emergency declarations.",
                                )
                            ],
                            href="https://cape.mysociety.org/councils/?name=&declared_emergency=&has_plan=&promise_combined=&authority_type=&region=North+East&geography=&population=&sort=name",
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
                        html.H5("Council Climate Plan Scorecards"),
                        html.P(
                            [
                                html.A(
                                    "Climate Emergency UK",
                                    href="https://www.climateemergency.uk/",
                                    target="_blank",
                                ),
                                " assessed plans according to 28 questions across nine sections, based on the expert-approved checklist for Council Action Plans. Click the image below to visit the website and view the scorecards.",
                            ]
                        ),
                        html.A(
                            [
                                html.Img(
                                    src=locations.get_link("transition_work_combined"),
                                    width="100%",
                                    alt="Click the image to view the Council Climate Plan Scorecards",
                                )
                            ],
                            href="https://www.councilclimatescorecards.uk/scoring/combined/",
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
                        big_projects,
                        gender_pay_gap,
                        climate_emerg_decs,
                    ]
                )
            ]
        )
    ]
)
