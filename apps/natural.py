import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

### Row 1: Land
natural_land = dbc.CardGroup(
    dbc.Card(
        [dbc.CardBody(html.H4(children="Land"))],
        outline=True,
        className="py-2 border-success",
    ),
    className="mb-2",
)

card00 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("Habitat extent and condition", className="card-title"),
                html.I(
                    className="bi bi-arrow-up",
                    style={"font-size": "5rem", "color": "mediumseagreen"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-success align-content-center",
)

card01 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("Landscape profiles", className="card-title align-middle"),
                html.I(
                    className="bi bi-arrow-right",
                    style={"font-size": "5rem", "color": "orange"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-success",
)

card02 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("Green infrastructure", className="card-title"),
                html.I(
                    className="bi bi-arrow-up",
                    style={"font-size": "5rem", "color": "mediumseagreen"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-success",
)

card03 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("Northumbria University [placeholder]", className="card-title"),
                html.I(
                    className="bi bi-arrow-up",
                    style={"font-size": "5rem", "color": "mediumseagreen"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-success",
)

natural_land_summary = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("Land", className="card-title py-3 text-center"),
                dbc.Button(
                    "Explore indicators",
                    href="/natural_land",
                    color="primary",
                    className="py-3 col-12 mx-auto",
                ),
            ]
        )
    ],
    outline=True,
    className="border-success",
)

cardrow1 = dbc.CardGroup(
    [card00, card01, card02, card03, natural_land_summary], className="mb-4"
)


#### Row 2: Water
natural_water = dbc.CardGroup(
    dbc.Card(
        [dbc.CardBody(html.H4(children="Water"))],
        outline=True,
        className="py-2 border-warning",
    ),
    className="mb-2",
)

card04 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("Fish counts", className="card-title"),
                html.I(
                    className="bi bi-arrow-up",
                    style={"font-size": "5rem", "color": "mediumseagreen"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-warning",
)

card05 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("Flood spend", className="card-title"),
                html.I(
                    className="bi bi-arrow-right",
                    style={"font-size": "5rem", "color": "orange"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-warning",
)

card06 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("River basin management", className="card-title"),
                html.I(
                    className="bi bi-arrow-right",
                    style={"font-size": "5rem", "color": "mediumseagreen"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-warning",
)

card07 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("Blue flag beaches", className="card-title"),
                html.I(
                    className="bi bi-arrow-right",
                    style={"font-size": "5rem", "color": "mediumseagreen"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-warning",
)

natural_water_summary = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("Water", className="card-title py-3 text-center"),
                dbc.Button(
                    "Explore indicators",
                    href="/natural_water",
                    color="primary",
                    className="py-3 col-12 mx-auto",
                ),
            ]
        )
    ],
    outline=True,
    className="border-warning",
)

cardrow2 = dbc.CardGroup(
    [card04, card05, card06, card07, natural_water_summary], className="mb-4"
)


#### Row 3: And also
natural_also = dbc.CardGroup(
    dbc.Card(
        [dbc.CardBody(html.H4(children="And also"))],
        outline=True,
        className="py-2 border-info",
    ),
    className="mb-2",
)

card08 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("Clean air", className="card-title"),
                html.I(
                    className="bi bi-arrow-up",
                    style={"font-size": "5rem", "color": "red"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-info",
)

card09 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("Regional and national atlases", className="card-title"),
                html.I(
                    className="bi bi-arrow-up",
                    style={"font-size": "5rem", "color": "mediumseagreen"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-info",
)

card10 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("Changing weather", className="card-title"),
                html.I(
                    className="bi bi-arrow-down",
                    style={"font-size": "5rem", "color": "red"},
                ),
            ]
        )
    ],
    outline=True,
    className="border-info",
)

natural_also_summary = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H5("And also", className="card-title py-3 text-center"),
                dbc.Button(
                    "Explore indicators",
                    href="/natural_also",
                    color="primary",
                    className="py-3 col-12 mx-auto",
                ),
            ]
        )
    ],
    outline=True,
    className="border-info",
)

cardrow3 = dbc.CardGroup(
    [card08, card09, card10, natural_also_summary], className="mb-4"
)


layout = dbc.Container(
    [
        dbc.Row(dbc.Col(html.H1(children="Natural Capital"), className="py-3")),
        dbc.Row(
            dbc.Col(
                html.H4(
                    children="Shows the growth in the quality and value of our natural environment"
                ),
                className="mb-2",
            )
        ),
        dbc.Row(
            dbc.Col(
                html.P(
                    children="This indicator will collect metrics and data to show changes in our natural assets that are happening because of regional efforts to become England’s Greenest Region. This includes changes in quantity and quality of resources and species in our region and the ability of our landscapes to store carbon. Overtime it will begin to show the services we get from nature and the value of these services to us as individuals and businesses."
                ),
                className="mb-4",
            ),
        ),
        dbc.Row(natural_land),
        dbc.Row(cardrow1),
        dbc.Row(natural_water),
        dbc.Row(cardrow2),
        dbc.Row(natural_also),
        dbc.Row(cardrow3),
    ]
)
