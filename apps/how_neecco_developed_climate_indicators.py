import plotly.graph_objects as go
import pandas as pd

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import plotly.express as px

from app import app, neecco_palette


# Sections

# Section 1: page title
title = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1(
                            "How NEECCo developed climate indicators", className="py-3"
                        )
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                html.P(
                    "NEECCo – the North East England Climate Coalition - was formed in 2019, adopting the mission of “Becoming England’s Greenest Region”, with the aims of addressing the climate emergency and the ecological collapse while advocating for a just transition. If we were going to make such claims we needed to understand if as a region we were doing enough of the right things, fast enough (spoiler alert: we’re not yet). And so the Indicators Project was initiated."
                ),
                html.P(
                    "During the development of the dashboard several hundred people have been involved –thanks to them all. Initial conversations with a wide range of people from across the region led to a mock up, paper version of the dashboard. The issues of creating an on-line resource were considered through a Hackathon organised with National Innovation Centre for Data – NICD - to coincide with the UN CoP 26 in Glasgow, and subsequently the Analysts Network North East 2022 Challenge. During the summer of 2022 a set of thematic expert roundtables helped to identify and shape the final content. The invaluable support and technical input from NICD has produced and populated the current visualisation."
                ),
                html.P(
                    "Since its production the mock up has been discussed with multiple and diverse audiences. Consistently there have been two responses. People tend to say either “that’s interesting, I’d never thought about …”, or “yes but shouldn’t this (issue/data) also be included?”.  So it has become clear that this resource is most useful for informing and enabling better conversations. Informed discussion is not enough, but it is necessary if we are to make the fundamental changes that are essential."
                ),
                html.P(
                    "The project has been funded by NEECCo with specific support from Sage Group and the Environment Agency. NICD’s work has been funded by NEECCo and Sage Group, at a rate subsidized by the North of Tyne Combined Authority. The project was initiated by Claire Thompson and subsequently led by Chris Ford. The NICD team of Hollie Johnson and Louise Braithwaite was led by Peter Michalak. Thanks to them all."
                ),
                html.P(
                    "If you would like to get in touch please email vonne@vonne.org.uk."
                ),
            ]
        ),
    ],
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
                    ]
                )
            ]
        ),
    ]
)
