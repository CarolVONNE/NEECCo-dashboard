from dash import html
import dash_bootstrap_components as dbc
from app import app, neecco_palette

import pandas as pd
import plotly.express as px
import dash_core_components as dcc

## import data loader helper
from locations_loader import LocationsLoader

# initialise locations loader
locations = LocationsLoader()
fish_data = pd.read_csv(locations.get_link("natural_water_fish"))

# create figures
fig_fish = px.line(
    fish_data,
    x="Month",
    y="Count",
    color="River",
    markers=True,
    color_discrete_sequence=neecco_palette,
    template="simple_white",
    labels={"Count": "Monthly fish count"},
)
fig_fish.update_traces(connectgaps=True)

# Sections


# Section 1: page title
title = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("Nature: Water ", className="py-3"),
                        html.P(
                            [
                                "About 70% of the Earth’s surface is covered with water. Within the region there is work focused on our estuaries, such as ",
                                html.Span(
                                    [
                                        html.A(
                                            "https://www.groundwork.org.uk/projects/revitalising-our-estuaries/",
                                            href="https://www.groundwork.org.uk/projects/revitalising-our-estuaries/",
                                            target="_blank",
                                        )
                                    ]
                                ),
                                " as well as further upstream. The ‘Northumbria River Basin District’ covers the whole of our region, betwixt Tweed and Tees. There have been monthly fish counts over several decades on the Tyne and the Wear, with the Tees being added more recently.",
                            ]
                        ),
                        html.P(
                            [
                                "How the oceans will change with man-made climate change is unknown; although there will continue to be rises in sea levels (see ",
                                html.Span(
                                    [
                                        html.A(
                                            "Sea level rise and coastal flood risk maps -- a global screening tool by Climate Central",
                                            href="https://coastal.climatecentral.org/",
                                            target="_blank",
                                        )
                                    ]
                                ),
                                "). Within the region there are also significant risks from surface water.",
                            ]
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
                                html.A(
                                    html.P("River basin management plan"),
                                    href="#section1",
                                )
                            ),
                            html.Li(html.A(html.P("Fish counts"), href="#section2")),
                            html.Li(html.A(html.P("Flood risk map"), href="#section3")),
                        ]
                    ),
                ]
            ),
        ),
    ],
    class_name="container-type1",
)


# Section 1: River basin management plan
river_basin = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H2("River basin management plan")])]),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3(
                            "Northumbria River Basin District - Management catchments"
                        ),
                        html.A(
                            [
                                html.Img(
                                    src=locations.get_link("nature_water_river_basin"),
                                    width="100%",
                                )
                            ],
                            href="https://environment.data.gov.uk/catchment-planning/RiverBasinDistrict/3",
                            target="_blank",
                            title="Click on the image to view the DEFRA data",
                        ),
                        html.A(
                            [
                                html.P(
                                    "Northumbria River Basin District - Management catchments"
                                )
                            ],
                            href="https://environment.data.gov.uk/catchment-planning/RiverBasinDistrict/3",
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

# Section 2: Fish counts/better
fish_counts = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H2("Fish counts")])]),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H5("Fish counts in the North East"),
                        dcc.Graph(
                            id="grph1",
                            figure=fig_fish,
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
                            href="https://www.gov.uk/government/statistical-data-sets?keywords=fish%20counts",
                            target="_blank",
                        ),
                    ]
                ),
            ]
        ),
    ],
    id="section2",
    class_name="container-type1",
)

# Section 3: Flood risk map
flood_risk_map = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H2("Flood risk map")])]),
        dbc.Row(
            [
                html.A(
                    [
                        html.Img(
                            src=locations.get_link("nature_water_flooding"),
                            width="100%",
                        )
                    ],
                    href="https://environment.data.gov.uk/DefraDataDownload/?mapService=EA/RiskOfFloodingFromRiversAndSea&Mode=spatial",
                    target="_blank",
                    title="Click on the image to view the DEFRA data",
                ),
                html.A(
                    [html.P("Risk of Flooding from Rivers and Sea (DEFRA)")],
                    href="https://environment.data.gov.uk/DefraDataDownload/?mapService=EA/RiskOfFloodingFromRiversAndSea&Mode=spatial",
                    target="_blank",
                ),
                html.A(
                    [html.P("Gov.UK - learn more about flood risk")],
                    href="https://check-long-term-flood-risk.service.gov.uk/map",
                    target="_blank",
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
                        river_basin,
                        fish_counts,
                        flood_risk_map,
                    ]
                )
            ]
        )
    ]
)
