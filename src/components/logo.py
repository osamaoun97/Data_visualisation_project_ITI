from dash import html
import dash_bootstrap_components as dbc
from const import *


def logo(app):
    return dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardImg(
                            src=image_source("netflix_logo.png"),
                            style={
                                "height": "80%",
                                "width": "25%",
                                "padding-top": "5px",
                            },
                            className="align-self-center",
                            top=True,
                        ),
                    ],
                )
            )
        ]
    )
