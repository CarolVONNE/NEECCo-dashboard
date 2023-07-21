from tracemalloc import start

from dash import html
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
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("Nature: Land ", className="py-3"),
                    ]
                ),
                dbc.Row(
                    [
                        html.P(
                            'Natural England’s Area Profiles "cover areas that share similar landscape characteristics, and which follow natural lines in the landscape rather than administrative boundaries". Although about 10 years old, they provide descriptions of each area as well as a statement of environmental opportunity.'
                        ),
                        html.P(
                            "One area of opportunity that is becoming increasingly important with net zero aspirations is the different amount of carbon that is or could be held in different habits. This was the subject of a small piece of research undertaken with NEECCo by colleagues at Northumbria University and Groundwork Trust."
                        ),
                        html.P(
                            [
                                "Natural England’s green infrastructure map provides an accessible route into current practice with their Geoportal ",
                                html.Span(
                                    [
                                        html.A(
                                            "(Natural England Open Data Geoportal (arcgis.com))",
                                            href="https://naturalengland-defra.opendata.arcgis.com/",
                                        )
                                    ]
                                ),
                                " giving access to their published data.  Defra’s MAGIC website provides authoritative geographic information about the natural environment from across government. The ONS published some experimental estimates (2022) using the System of Environmental-Economic Accounting for Ecosystem Accounting.",
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
                                            html.P("National Character Area profiles"),
                                            href="#section1",
                                        )
                                    ),
                                    html.Li(
                                        html.A(
                                            html.P("Habitat extent and condition"),
                                            href="#section2",
                                        )
                                    ),
                                    html.Li(
                                        html.A(
                                            html.P("Counting Carbon"),
                                            href="#section3",
                                        )
                                    ),
                                ]
                            ),
                        ]
                    ),
                ),
            ]
        )
    ],
    class_name="container-type1",
)


# Section: Landscape profiles
landscape_profiles = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col([html.H2("National Character Area profiles")]),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            "This Character Area interactive map for North East England displays 15 distinct regions referred to as National Character Areas (NCAs). These NCAs are fundamental divisions of the landscape that establish a cohesive countryside character, serving as a foundation for developing strategies for ecological and landscape-related matters. The Character Area framework is used to define and establish objectives for the countryside, as well as its planning and management."
                        ),
                        html.P(
                            "Further information can be obtained by clicking on the region of interest and following the provided link."
                        ),
                        html.Div(
                            [
                                html.Iframe(
                                    src=locations.get_link(
                                        "nature_land_landscape_folium_map"
                                    ),
                                    width="100%",
                                    height="750",
                                )
                            ]
                        ),
                        html.A(
                            [
                                html.H5(
                                    "Source: Natural England: National Character Areas"
                                )
                            ],
                            href="https://www.gov.uk/government/publications/national-character-area-profiles-data-for-local-decision-making/national-character-area-profiles#ncas-in-north-east-england",
                            target="_blank",
                        ),
                    ]
                )
            ]
        ),
    ],
    id="section1",
    class_name="container-type1",
)

# Section: Habitat extent and condition
habitat_content = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Habitat extent and condition"),
                        # html.H3(
                        #     "Map of woodland, urban, and semi-natural grassland broad habitats"
                        # ),
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3("DEFRA: MAGIC interactive map"),
                        html.P(
                            "The MAGIC website provides authoritative geographic information about the natural environment from across government. The information covers rural, urban, coastal and marine environments across Great Britain. It is presented in an interactive map which can be explored using various mapping tools that are included."
                        ),
                        html.A(
                            [html.H5("Natural England: Open Data Geoportal")],
                            href=locations.get_link("natural_land_defra_data"),
                            target="_blank",
                        ),
                        html.A(
                            [
                                html.H5(
                                    "Natural England: Green Infrastructure Interactive Map"
                                )
                            ],
                            href=locations.get_link(
                                "natural_land_green_infrastructure"
                            ),
                            target="_blank",
                        ),
                        html.A(
                            [
                                html.Img(
                                    src=locations.get_link(
                                        "natural_land_habitat_magic_map"
                                    ),
                                    width="95%",
                                ),
                                html.H5("Source: MAGIC map"),
                            ],
                            href=locations.get_link(
                                "natural_land_habitat_magic_map_link"
                            ),
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
                        html.H3("Natural England Infrastructure"),
                        html.P(
                            "Showing Access to Nature Close2Home and Environment Agency bathing beaches using the layering options on left hand side."
                        ),
                        html.A(
                            [
                                html.Img(
                                    src=locations.get_link(
                                        "natural_land_infrastructure"
                                    ),
                                    width="95%",
                                ),
                                html.H5(
                                    "Data Source: Natural England - Green Infrastructure"
                                ),
                            ],
                            href="https://designatedsites.naturalengland.org.uk/GreenInfrastructure/Map.aspx",
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

# Section 6: Neecco/northumb univ
neecco = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H2("Counting Carbon")])]),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.A(
                            [
                                html.Img(
                                    src=locations.get_link(
                                        "natural_land_land_coverage"
                                    ),
                                    width="100%",
                                ),
                            ]
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
                            "Working with NEECCo in a new pilot project, Groundwork NE & Cumbria collaborated in partnership with Northumbria University to count the carbon locked up in the habitats and land cover types of the North East. This project supports NEECCo's promise to respond to the climate emergency by empowering the region with knowledge and resources to deliver change. Improving our understanding of carbon sequestration and storage is imperative if we are to meet the goals in the Paris climate agreement, and in North East England this understanding will need to be at the heart of decision making on land management in the environment."
                        ),
                        html.P(
                            "With thanks to Dr Andy Suggitt, Northumbria University and Gaby McKay Jones."
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
                        landscape_profiles,
                        habitat_content,
                        neecco,
                    ]
                )
            ]
        )
    ]
)
