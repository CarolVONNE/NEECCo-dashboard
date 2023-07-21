import plotly.graph_objects as go
import pandas as pd

from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

from app import app, neecco_palette

from locations_loader import LocationsLoader


# initialise locations loader
locations = LocationsLoader()

# data
fuel_poverty = pd.read_csv(locations.get_link("transition_home_fuel_poverty"))


# create figures
fig_fuel_poverty = px.line(
    fuel_poverty,
    x="year",
    y="proportion",
    line_dash="region",
    markers=True,
    color_discrete_sequence=neecco_palette,
    template="simple_white",
    labels={
        "year": "Year",
        "region": "Region",
        "proportion": "Percentage of homes in fuel poverty",
    },
)
newnames = {"North East": "North East", "All households": "UK"}
fig_fuel_poverty.for_each_trace(
    lambda t: t.update(
        name=newnames[t.name],
        legendgroup=newnames[t.name],
        hovertemplate=t.hovertemplate.replace(t.name, newnames[t.name]),
    )
)

# Sections

# Section 1: page title
title = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H1("Just Transition: At Home", className="py-3")])]),
        dbc.Row(
            dbc.Col(
                [
                    html.H4("Page content"),
                    html.Ul(
                        [
                            html.Li(html.A(html.P("Fuel poverty"), href="#section1")),
                            html.Li(html.A(html.P("Food"), href="#section2")),
                        ]
                    ),
                ]
            ),
        ),
    ],
    class_name="container-type1",
)

# Section 3: Fuel poverty
fuel_poverty = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H2("Fuel poverty")])]),
        dbc.Row(
            [
                html.P(
                    [
                        "There are several definitions of fuel poverty. The UK government use the LILEE indicator as explained below. National Energy Action, which is based in Newcastle, are an important source of expertise: see ",
                        html.Span(
                            [
                                html.A(
                                    "https://www.nea.org.uk/",
                                    href="https://www.nea.org.uk/",
                                )
                            ]
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        html.H5("Percentage of homes in fuel poverty"),
                        dcc.Graph(
                            id="grph3",
                            figure=fig_fuel_poverty,
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
                            href="https://www.gov.uk/government/statistics/fuel-poverty-trends-2022",
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
                        html.H5("About fuel poverty"),
                        html.P(
                            "Fuel poverty in England is measured using the Low Income Low Energy Efficiency (LILEE) indicator. Under this indicator, a household is considered to be fuel poor if: "
                        ),
                        html.Ul(
                            [
                                html.Li(
                                    "they are living in a property with a fuel poverty energy efficiency rating of band D or below, and "
                                ),
                                html.Li(
                                    "when they spend the required amount to heat their home, they are left with a residual income below the official poverty line "
                                ),
                            ]
                        ),
                        html.P(
                            "There are 3 important elements in determining whether a household is fuel poor:"
                        ),
                        html.Ul(
                            [
                                html.Li("household income"),
                                html.Li("household energy requirements "),
                                html.Li("fuel prices"),
                            ]
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

# Section 4: Food
food = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H2("Food")])]),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            [
                                html.Span(
                                    [
                                        html.A(
                                            "The Trussell Trust",
                                            href="https://www.trusselltrust.org/get-help/find-a-foodbank/",
                                        )
                                    ]
                                ),
                                " supports a nationwide network of food banks",
                                '. There is also a network of independent food aid providers whose vision is of "a country without the need for charitable food aid where adequate and nutritious food is affordable to all." ',
                                html.Span(
                                    [
                                        html.A(
                                            "The Food Foundation",
                                            href="https://foodfoundation.org.uk/initiatives/food-prices-tracking",
                                        )
                                    ]
                                ),
                                " is focused on changing the ‘food system’, along with more local networks including Sustainable Food Places. ",
                            ]
                        ),
                        html.A(
                            [
                                html.Img(
                                    src=locations.get_link("just_transition_home_food"),
                                    width="80%",
                                    alt="Sustainable Food Places",
                                    title="Click on the image to visit Sustainable Food Places",
                                )
                            ],
                            href="https://www.sustainablefoodplaces.org/members/",
                            target="_blank",
                        ),
                        html.P(
                            html.A(
                                "Sustainable Food places",
                                href="https://www.sustainablefoodplaces.org/members/",
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
                        html.Iframe(
                            src="https://www.google.com/maps/d/embed?mid=15mnlXFpd8-x0j4O6Ck6U90chPn4bkbWz&ehbc=2E312F&ll=55.07080913792946%2C-1.2056044031249988&z=8",
                            width="100%",
                            height="630px",
                        ),
                        html.A(
                            [html.P("Independent Food Aid Network: Food banks map")],
                            href="https://www.foodaidnetwork.org.uk/independent-food-banks-map",
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
layout = dbc.Container([dbc.Row([dbc.Col([title, fuel_poverty, food])])])
