import os

from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import server
from app import app

## import data loader helper
from locations_loader import LocationsLoader

# import all pages in the app
from apps import (
    home,
    how_neecco_developed_climate_indicators,
    carbon,
    economic,
    natural,
    social,
    transition,
    natural_land,
    natural_water,
    natural_also,
    economic_also,
    economic_circular,
    economic_energy,
    transition_also,
    transition_home,
    transition_work,
    social_also,
    social_communities,
    social_nature,
)

# header across all pages
headbar = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Img(src="/assets/NEECCo.jpeg", height="50px"),
                    xs=12,
                    sm=12,
                    md=12,
                    lg=6,
                    xl=6,
                ),
                dbc.Col(html.H1("Indicators"), xs=12, sm=12, md=12, lg=6, xl=6),
            ],
            class_name="py-3",
        ),
    ]
)

navbar32 = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/home")),
        dbc.NavItem(dbc.NavLink("Carbon", href="/carbon")),
        dbc.DropdownMenu(
            children=[
                # dbc.DropdownMenuItem("Nature", href="/natural"),
                dbc.DropdownMenuItem("Land", href="/natural_land"),
                dbc.DropdownMenuItem("Water", href="/natural_water"),
                dbc.DropdownMenuItem("And also", href="/natural_also"),
            ],
            nav=True,
            in_navbar=True,
            label="Nature",
        ),
        dbc.DropdownMenu(
            children=[
                # dbc.DropdownMenuItem("Economic", href="/economic"),
                dbc.DropdownMenuItem(
                    "Towards a circular economy", href="/economic_circular"
                ),
                dbc.DropdownMenuItem("Energy", href="/economic_energy"),
                dbc.DropdownMenuItem("And also", href="/economic_also"),
            ],
            nav=True,
            in_navbar=True,
            label="Economic",
        ),
        dbc.DropdownMenu(
            children=[
                # dbc.DropdownMenuItem("Social", href="/social"),
                dbc.DropdownMenuItem("Our communities", href="/social_communities"),
                dbc.DropdownMenuItem("Engagement with nature", href="/social_nature"),
                dbc.DropdownMenuItem("And also", href="/social_also"),
            ],
            nav=True,
            in_navbar=True,
            label="Social",
        ),
        dbc.DropdownMenu(
            children=[
                # dbc.DropdownMenuItem("Transition", href="/transition"),
                dbc.DropdownMenuItem("At home", href="/transition_home"),
                dbc.DropdownMenuItem("At work", href="/transition_work"),
                dbc.DropdownMenuItem("And also", href="/transition_also"),
            ],
            nav=True,
            in_navbar=True,
            label="Just Transition",
        ),
    ],
    links_left="True",
    # brand="Climate Dashboard",
    # brand_href="#",
    color="primary",
    dark=True,
)

footbar = dbc.NavbarSimple(
    children=[
        dbc.NavLink("How NEECCO developed climate indicators", href="/how_neecco_developed_climate_indicators"),
        dbc.NavLink("Visit the NEECCo website", href="https://neecco.org.uk"),
        dbc.NavLink(
            html.I(className="bi bi-github", style={"font-size": "1.5rem"}),
            href="https://github.com/CarolVONNE/NEECCo-dashboard",
            external_link=True,
        ),
        dbc.NavLink(
            "This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License",
            href="http://creativecommons.org/licenses/by-nc-sa/4.0/",
        ),
        dbc.NavLink(
            html.Img(
                src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png",
                alt="Creative Commons Licence",
                style={"border-width": "0"},
            ),
            href="http://creativecommons.org/licenses/by-nc-sa/4.0/",
            external_link=True,
        ),
    ],
    links_left="True",
    color="primary",
    dark=True,
)

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        headbar,
        navbar32,
        # navbar,
        html.Div(id="page-content"),
        footbar
        # html.Footer(html.A('How NEECCo developed its metrics', href="")),
    ]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/carbon":
        return carbon.layout
    if pathname == "/how_neecco_developed_climate_indicators":
        return how_neecco_developed_climate_indicators.layout
    if pathname == "/transition":
        return transition.layout
    elif pathname == "/social":
        return social.layout
    elif pathname == "/natural":
        return natural.layout
    elif pathname == "/economic":
        return economic.layout
    elif pathname == "/natural_land":
        return natural_land.layout
    elif pathname == "/natural_water":
        return natural_water.layout
    elif pathname == "/natural_also":
        return natural_also.layout
    elif pathname == "/economic_circular":
        return economic_circular.layout
    elif pathname == "/economic_energy":
        return economic_energy.layout
    elif pathname == "/economic_also":
        return economic_also.layout
    elif pathname == "/transition_home":
        return transition_home.layout
    elif pathname == "/transition_work":
        return transition_work.layout
    elif pathname == "/transition_also":
        return transition_also.layout
    elif pathname == "/social_communities":
        return social_communities.layout
    elif pathname == "/social_nature":
        return social_nature.layout
    elif pathname == "/social_also":
        return social_also.layout
    else:
        return home.layout


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8085, debug=True)
