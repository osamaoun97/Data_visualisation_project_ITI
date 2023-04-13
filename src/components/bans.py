from dash import html
import dash_bootstrap_components as dbc
from const import *
from ..graphs import bans_graph


def bans(app):
    movie_ban = dbc.Col(
        [
            dbc.Card(
                [
                    dbc.CardImg(
                        src=image_source('final_movie.png'),
                        style={"height": "2%", "width": "25%", "padding-top": "5px"},
                        className="align-self-center",
                        top=True,
                    ),
                    dbc.CardBody(
                        [
                            html.H6(
                                "Number of Movies",
                                className="card-text",
                                style={
                                    "font-size": "20px",
                                    "color": MOV_COLOR,
                                    "font-family": "Sans-serif",
                                    "font-weight": "bold",
                                },
                            ),
                            html.H1(
                                f"{bans_graph.ban_movies()}",
                                id="num_movies",
                                style={
                                    "font-size": "30px",
                                    "color": MOV_COLOR,
                                    "font-weight": "bold",
                                },
                            ),
                        ]
                    ),
                ],
                style={
                    "width": "26rem",
                    "box-shadow": "0 4px 8px 0 rgba(0,0,0,0.2)",
                    "border-radius": "5px",
                },
            )
        ],
        width=4,
        style={
            "height": "220px",
            "background-color": "transparent",
            "text-align": "center",
        },
    )

    show_ban = dbc.Col(
        [
            dbc.Card(
                [
                    dbc.CardImg(
                        src=image_source('final_tvshow.png'),
                        style={"height": "2%", "width": "25%", "padding-top": "5px"},
                        className="align-self-center",
                        top=True,
                    ),
                    dbc.CardBody(
                        [
                            html.H6(
                                "Number of TV Shows",
                                className="card-text",
                                style={
                                    "font-size": "20px",
                                    "color": " #E50914",
                                    "font-family": "Sans-serif",
                                    "font-weight": "bold",
                                },
                            ),
                            html.H1(
                                f"{bans_graph.ban_shows()}",
                                id="num_tv_shows",
                                style={
                                    "font-size": "30px",
                                    "color": " #E50914",
                                    "font-weight": "bold",
                                },
                            ),
                        ]
                    ),
                ],
                style={
                    "width": "26rem",
                    "box-shadow": "0 4px 8px 0 rgba(0,0,0,0.2)",
                    "border-radius": "5px",
                },
            )
        ],
        width=4,
        style={
            "height": "220px",
            "background-color": "transparent",
            "text-align": "center",
        },
    )

    countries_ban = dbc.Col(
        [
            dbc.Card(
                [
                    dbc.CardImg(
                        src=image_source("final_world.png"),
                        style={"height": "2%", "width": "25%", "padding-top": "5px"},
                        className="align-self-center",
                        top=True,
                    ),
                    dbc.CardBody(
                        [
                            html.H6(
                                "Number of Countries",
                                className="card-text",
                                style={
                                    "font-size": "20px",
                                    "color": "#ffffff",
                                    "font-family": "Sans-serif",
                                    "font-weight": "bold",
                                },
                            ),
                            html.H1(
                                f"{bans_graph.ban_countries()}",
                                id="num_countries",
                                style={
                                    "font-size": "30px",
                                    "color": "#ffffff",
                                    "font-weight": "bold",
                                },
                            ),
                        ]
                    ),
                ],
                style={
                    "width": "26rem",
                    "box-shadow": "0 4px 8px 0 rgba(0,0,0,0.2)",
                    "border-radius": "5px",
                },
            )
        ],
        width=4,
        style={
            "height": "220px",
            "background-color": "transparent",
            "text-align": "center",
        },
    )

    return dbc.Row([movie_ban, show_ban, countries_ban])
