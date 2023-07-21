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
data_gdhi = pd.read_csv(locations.get_link("social_communities_gdhi"))

# create figures
fig_gdhi = px.bar(
    data_gdhi,
    y="Region",
    x="GDHI per head",
    height=400,
    color_discrete_sequence=neecco_palette,
    template="simple_white",
    orientation="h",
    labels={"GDHI per head": "GDHI per head (£)"},
)

# load data
fsm_data = pd.read_csv(locations.get_link("transition_also_fsm"))

# create figures
fig_fsm = px.line(
    fsm_data,
    x="Year",
    y="Percent of pupils",
    line_dash="Region",
    markers=True,
    color_discrete_sequence=neecco_palette,
    template="simple_white",
    line_dash_sequence=["dot", "solid"],
)


# Sections

# Section 1: page title
title = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H1("Social: Our Communities", className="py-3")])]),
        dbc.Row(
            [
                html.P(
                    '"Poverty is not natural. It is man-made and it can be overcome and eradicated by the action of human beings." (Mandela, 2005)'
                ),
                html.P(
                    "Within the North East child poverty is increasing as the regional commission documents. Free school meals are widely seen as a key measure of poverty, although many families do not claim this entitlement."
                ),
                html.P(
                    [
                        "For a broader overview of poverty see the ",
                        html.Span(
                            [
                                html.A(
                                    "Jospeh Rowntree Foundation’s Essential Guide to Understanding Poverty in the UK",
                                    href="https://www.jrf.org.uk/report/uk-poverty-2023",
                                    target="_blank",
                                )
                            ]
                        ),
                        ". ",
                        html.Span(
                            [
                                html.A(
                                    "The Local Government Association website",
                                    href="https://lginform.local.gov.uk/reports/view/lga-research/ficlga-research-report-financial-hardship-and-economic-vulnerability?mod-area=E06000047&mod-group=AllUnitaryLaInCountry_England&mod-type=namedComparisonGroup",
                                    target="_blank",
                                )
                            ]
                        ),
                        " provides reports that can be customised to each local authority area or the region with a wide range of possible comparator geographies.",
                    ]
                ),
                html.P(
                    [
                        "There are clear relationships between poverty and ill health, as illustrated in the ",
                        html.Span(
                            [html.A("Health Inequalities Dashboard", href="#section3")]
                        ),
                        " and the ",
                        html.Span(
                            [html.A("Regional Health profile", href="#section4")]
                        ),
                        ". The Environment Agency’s report ",
                        html.Span(
                            [
                                html.A(
                                    "‘State of the environment: health, people and the environment’",
                                    href="https://www.gov.uk/government/publications/state-of-the-environment/state-of-the-environment-health-people-and-the-environment",
                                    target="_blank",
                                )
                            ]
                        ),
                        " provides a useful overview on a national (English) level.",
                    ]
                ),
            ]
        ),
        dbc.Row(
            dbc.Col(
                [
                    html.H4("Page content"),
                    html.Ul(
                        [
                            html.Li(html.A(html.P("Poverty"), href="#section1")),
                            html.Li(
                                html.A(html.P("Free School Meals"), href="#section2")
                            ),
                            html.Li(
                                html.A(html.P("Health inequalities"), href="#section3")
                            ),
                            html.Li(
                                html.A(
                                    html.P("Regional Health Profile"), href="#section4"
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

# Section 1: Poverty
poverty = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H2("Poverty")])]),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.A(
                            [
                                html.Img(
                                    src=locations.get_link(
                                        "social_communities_child_poverty"
                                    ),
                                    width="100%",
                                    title="Click on the screenshot to go to the website",
                                )
                            ],
                            href="https://www.nechildpoverty.org.uk/facts/",
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
                        html.H3("North East Child Poverty"),
                        html.P(
                            "This site provides an overview of findings published by the End Child Poverty coalition. Key headlines include:"
                        ),
                        html.Ul(
                            [
                                html.Li(
                                    "In 2020/21, the North East overtook London to have the highest rate of child poverty in the UK, at 38% - up from 37% the year before. This equates to just over 11 children in a classroom of 30."
                                ),
                                html.Li(
                                    "The 2020/21 North East rise continues a longer-term trend, with the region experiencing by far the steepest increases in child poverty in the UK in recent years."
                                ),
                                html.Li(
                                    "In previous years, two areas in the North East (Newcastle and Middlesbrough) featured in the list of the 20 local authorities with the highest child poverty rates in the UK. For 2020/21, this list now includes Newcastle (42.4%), Middlesbrough (41.2%), Sunderland (39.7%), Redcar and Cleveland (39.3%), South Tyneside (39.1%) and Hartlepool (39.0%)."
                                ),
                                html.Li(
                                    "One third of the North East’s Parliamentary constituencies now have a child poverty rate of 40% or above."
                                ),
                            ]
                        ),
                        html.A(
                            html.P("North East Child Poverty"),
                            href="https://www.nechildpoverty.org.uk/facts/",
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
                        html.H5(
                            "Regional gross disposable household income (GDHI), 2019"
                        ),
                        dcc.Graph(
                            id="grph1",
                            figure=fig_gdhi,
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
                            "Data Source: Office for National Statistics",
                            href="https://www.ons.gov.uk/economy/regionalaccounts/grossdisposablehouseholdincome/bulletins/regionalgrossdisposablehouseholdincomegdhi/1997to2019#gross-disposable-household-income-for-itl3-local-areas",
                            target="_blank",
                        ),
                    ]
                ),
            ]
        ),
    ],
    id="section1",
    class_name="container-type1",
)

# Section 4: Free school meals
free_school_meals = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col([html.H2("Free school meals")]),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            "Your child may be able to get free school meals if you get any of the following:"
                        ),
                        html.Ul(
                            [
                                html.Li("Income Support"),
                                html.Li("Income-based Jobseeker’s Allowance"),
                                html.Li(
                                    "Income-related Employment and Support Allowance"
                                ),
                                html.Li(
                                    "Support under Part VI of the Immigration and Asylum Act 1999"
                                ),
                                html.Li("The guaranteed element of Pension Credit"),
                                html.Li(
                                    "Child Tax Credit (provided you’re not also entitled to Working Tax Credit and have an annual gross income of no more than £16,190"
                                ),
                                html.Li(
                                    "Working Tax Credit run-on - paid for 4 weeks after you stop qualifying for Working Tax Credit"
                                ),
                                html.Li(
                                    "Universal Credit - if you apply on or after 1 April 2018 your household income must be less than £7,400 a year (after tax and not including any benefits you get"
                                ),
                            ]
                        ),
                        html.P(
                            "Children who get paid these benefits directly, instead of through a parent or guardian, can also get free school meals."
                        ),
                        html.P(
                            "Your child may also get free school meals if you get any of these benefits and your child is both: "
                        ),
                        html.Ul(
                            [
                                html.Li(
                                    "Younger than the compulsory age for starting school"
                                ),
                                html.Li("In full-time education"),
                            ]
                        ),
                        html.P(
                            html.A(
                                "Apply for free school meals",
                                href="https://www.gov.uk/apply-free-school-meals",
                                target="_blank",
                            )
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
                        html.H5("Percentage of pupils eligible for free school meals"),
                        dcc.Graph(
                            id="grph1",
                            figure=fig_fsm,
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
                            href="https://explore-education-statistics.service.gov.uk/find-statistics/school-pupils-and-their-characteristics#dataBlock-87182242-6c3a-4eb1-b5fc-d91da60207e9-charts",
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

# Section 2: Health inequalities
health_inequalities = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H2("Health inequalities")])]),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.A(
                            [
                                html.Img(
                                    src=locations.get_link(
                                        "social_communities_health_inequalities_dashboard"
                                    ),
                                    width="100%",
                                    title="Click on the screenshot to go to the dashboard",
                                )
                            ],
                            href="https://analytics.phe.gov.uk/apps/health-inequalities-dashboard/",
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
                        html.H3("Health Inequalities Dashboard"),
                        html.P(
                            "This dashboard includes data on an number of health inequality indicators. Users can explore and download data and produce plots. Indicators include:"
                        ),
                        html.Ul(
                            [
                                html.Li(
                                    "Healthy life expectancy (inequality measure only"
                                ),
                                html.Li("Infant mortality rate"),
                                html.Li("Low birth weight of term babies"),
                                html.Li("Smoking prevalence in adults"),
                                html.Li(
                                    "Percentage of children not achieving a good level of development at age 5"
                                ),
                                html.Li(
                                    "Self-reported wellbeing - people with a low satisfaction score"
                                ),
                            ]
                        ),
                        html.A(
                            [
                                html.P(
                                    "Health Inequalities - Dashboard from Office for Health Improvement and Disparities"
                                )
                            ],
                            href="https://analytics.phe.gov.uk/apps/health-inequalities-dashboard/",
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


regional_health = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H2("Regional Health Profile")])]),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            "This profile is a comprehensive review of health in the North East region. It provides data available to download as well as a number of illustrative figures. The profile includes the following sections:"
                        ),
                        html.Ul(
                            [
                                html.Li("Overview of the population of the region"),
                                html.Li("COVID-19"),
                                html.Li("Mortality and life expectancy"),
                                html.Li("Child health"),
                                html.Li("Adult health"),
                                html.Li("Risk factors associated with ill health"),
                                html.Li("The wider determinants of health"),
                                html.Li("Health protection"),
                            ]
                        ),
                        html.A(
                            [
                                html.P(
                                    "Health Profile for the North East of England 2021 - Office for Health Improvement and Disparities"
                                )
                            ],
                            href="https://fingertips.phe.org.uk/static-reports/health-profile-for-england/regional-profile-north_east.html",
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
                                        "social_communities_regional_health_profile"
                                    ),
                                    width="100%",
                                    title="Click on the screenshot to go to the report",
                                )
                            ],
                            href="https://fingertips.phe.org.uk/static-reports/health-profile-for-england/regional-profile-north_east.html",
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
                        poverty,
                        free_school_meals,
                        health_inequalities,
                        regional_health,
                    ]
                )
            ]
        )
    ]
)
