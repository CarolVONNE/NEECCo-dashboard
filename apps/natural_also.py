import plotly.graph_objects as go
import pandas as pd

from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px

from app import app, neecco_palette

## import data loader helper
from locations_loader import LocationsLoader

# initialise locations loader
locations = LocationsLoader()

df_changing_weather = pd.read_csv(
    locations.get_link("natural_and_also_changing_weather")
)


# MET office historical average yearly minimum and maximum temperatures
fig_changing_weather = px.scatter(
    df_changing_weather,
    x="year",
    y=["Average yearly minimum temperature", "Average yearly maximum temperature"],
    trendline="ols",
    template="simple_white",
    opacity=0.9,
    color_discrete_sequence=neecco_palette,
    labels={"year": "Year", "variable": "Type", "value": "℃"},
)
fig_changing_weather.update_traces(showlegend=True)

# Sections

# Section 1: page title
title = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H1("Nature: And Also", className="py-3")])]),
        dbc.Row(
            [
                html.P(
                    'A very wide range of information is available including via ERIC, the region’s Environmental Records and Information Centre. With new public sector Duties and strategies around nature the regional Biodiversity Audit produced in 2001 provides an important source of longer term perspectives.'
                ),
                
                html.P(
                    [
                        "Long term perspectives are available for the weather patterns in Durham City, where data has been gathered for more than 140 years. The Environment Agency’s (established in 1996) portal provides access to a considerable range of data."
                    ]
                ),
                html.P(
                    [
                        "Defra’s Pollution Forecast map is an \"interactive tool (that) allows you to explore ambient air quality concentration data from Defra's national Pollution Climate Mapping modelling.\" The Clean Air Hub, brought to you by Global Action Plan, gives a broader context."
                    ]
                ),
                html.P(
                    [
                        'The Joint Nature Conservation Committee "is the public body that advises the UK Government and devolved administrations on UK-wide and international nature conservation." ',
                        html.Span(
                            [
                                html.A(
                                    "https://jncc.gov.uk/our-role/",
                                    href="https://jncc.gov.uk/our-role/",
                                )
                            ]
                        ),
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
                            html.Li(
                                html.A(
                                    html.P(
                                        "Regional and national atlases/repositories"
                                    ),
                                    href="#section2",
                                )
                            ),
                            html.Li(
                                html.A(html.P("Changing weather"), href="#section3")
                            ),
                            html.Li(
                                html.A(
                                    html.P(
                                        "Environment Agency Survey Open Data Index Catalogues"
                                    ),
                                    href="#section4",
                                )
                            ),
                            html.Li(html.A(html.P("Clean air"), href="#section1")),
                        ]
                    ),
                ]
            ),
        ),
    ],
    class_name="container-type1",
)

# Section 1: Clean air
clean_air = dbc.Container(
    [
        dbc.Row(
            [
                html.H2("Clean air"),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            "UK Air Quality Interactive Map by (Department for Environment Food & Rural Affairs)"
                        ),
                        html.A(
                            [
                                html.Img(
                                    src=locations.get_link("nature_also_air_quality"),
                                    width="95%",
                                ),
                            ],
                            href="https://uk-air.defra.gov.uk/data/gis-mapping/",
                            target="_blank",
                        ),
                        html.A(
                            [
                                "Source: UK Air Quality Interactive Map by (Department for Environment Food & Rural Affairs)",
                            ],
                            href="https://uk-air.defra.gov.uk/data/gis-mapping/",
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
                        html.P("Global Action Plan: Clean Air Hub"),
                        html.A(
                            [
                                html.Img(
                                    src=locations.get_link("nature_also_clean_air_hub"),
                                    width="95%",
                                ),
                            ],
                            href="https://www.cleanairhub.org.uk/home",
                            target="_blank",
                        ),
                        html.A(
                            [
                                "Source: Global Action Plan: Clean Air Hub",
                            ],
                            href="https://www.cleanairhub.org.uk/home",
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
                html.P(),
                html.P(
                    [
                        "Department for Environment Food & Rural Affairs provides air quality information and air pollution forecasts. To see forecast for the next five days for North East region follow ",
                        html.A(
                            [
                                "UK AIR: Air Information Resource link.",
                            ],
                            href="https://uk-air.defra.gov.uk/forecasting/locations?q=north+east+england",
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

# Section 2: Regional and national atlases/repositories
atlases_repositories = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H2("Regional and national atlases/repositories")])]),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.A(
                            [
                                html.Img(
                                    src="https://neeccostorage.blob.core.windows.net/indicatordata/natural/nature_also_biodiversity-audit-of-the-north-east.png",
                                    style={"width": "35%"},
                                )
                            ],
                            href="https://neeccostorage.blob.core.windows.net/indicatordata/natural/NE%20Biodiversity%20Audit%202001.pdf",
                        )
                    ],
                    style={"text-align": "center"},
                ),
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Div(
                                    "A Biodiversity Audit of the North East, Nick Brodin"
                                ),
                                html.A(
                                    [
                                        "Download (pdf)",
                                    ],
                                    href="https://neeccostorage.blob.core.windows.net/indicatordata/natural/NE%20Biodiversity%20Audit%202001.pdf",
                                    download="NE%20Biodiversity%20Audit%202001.pdf",
                                ),
                            ],
                            style={"padding-bottom": "25px"},
                        ),
                        html.H3("See also"),
                        html.Ul(
                            [
                                html.Li(
                                    [
                                        html.A(
                                            [
                                                "Environmental Records Information Centre North East",
                                            ],
                                            href="https://www.ericnortheast.org.uk/",
                                            target="_blank",
                                        )
                                    ]
                                ),
                                html.Li(
                                    [
                                        html.A(
                                            [
                                                "UKCEH Countryside Survey",
                                            ],
                                            href="https://countrysidesurvey.org.uk/about",
                                            target="_blank",
                                        )
                                    ]
                                ),
                                html.Li(
                                    [
                                        html.A(
                                            [
                                                "NBN atlas",
                                            ],
                                            href="https://nbnatlas.org/",
                                            target="_blank",
                                        )
                                    ]
                                ),
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
    id="section2",
    class_name="container-type1",
)


# Section 3: Changing Weather
changing_weather = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Changing Weather"),
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H5(
                            "Average yearly minimum and maximum historical temperature: Durham"
                        ),
                        dcc.Graph(
                            id="grph1",
                            figure=fig_changing_weather,
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
                            "Data Source: Met Office - Historic station data",
                            href="https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data",
                            target="_blank",
                        ),
                    ],
                    align="centre",
                )
            ]
        ),
    ],
    id="section3",
    class_name="container-type1",
)

# EA
ea = dbc.Container(
    [
        dbc.Row(
            [
                html.H2("Environment Agency Survey Open Data Index Catalogues"),
            ]
        ),
        dbc.Row(
            [
                html.A(
                    [html.Img(src=locations.get_link("nature_also_EA"), width="75%")],
                    href="https://environment.maps.arcgis.com",
                    target="_blank",
                ),
                html.A(
                    [
                        html.H5(
                            "Source: Environment Agency Survey Open Data Index Catalogues"
                        )
                    ],
                    href="https://environment.maps.arcgis.com",
                    target="_blank",
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
                        atlases_repositories,
                        changing_weather,
                        ea,
                        clean_air,
                    ]
                )
            ]
        )
    ]
)
