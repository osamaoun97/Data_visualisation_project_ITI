from ..graphs import actors_with_most_content, directors_with_most_content
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from const import *
from dash import html, dcc, Input, Output, State


def directors_actors_tabs(app):
    country_actors_tab_show = dbc.Tab(
        dbc.Card(
            [
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            html.Small(
                                "ㅤㅤSelect the country: ",
                                style={"font-size": "18px", "font-weight": "bold"},
                            ),
                            width=2,
                        ),
                        dbc.Col(
                            [
                                dcc.Dropdown(
                                    COUNTRIES_SHOWS,
                                    value="United States",
                                    id="dropdown_country1",
                                    multi=False,
                                    style={
                                        "color": "#000000",
                                        "background-color": "#cccccc",
                                    },
                                )
                            ],
                            width=3,
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col([dcc.Graph(id="highest_directors1")], width=6),
                        dbc.Col([dcc.Graph(id="highest_actors1")], width=6),
                    ]
                ),
            ]
        ),
        label="TV Show",
        activeTabClassName="fw-bold",
        label_style={"color": "#E50914"},
    )

    country_actors_tab_movie = dbc.Tab(
        dbc.Card(
            [
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            html.Small(
                                "ㅤㅤSelect the country: ",
                                style={"font-size": "18px", "font-weight": "bold"},
                            ),
                            width=2,
                        ),
                        dbc.Col(
                            [
                                dcc.Dropdown(
                                    COUNTRIES_MOVIES,
                                    value="United States",
                                    id="dropdown_country2",
                                    multi=False,
                                    style={
                                        "color": "#000000",
                                        "background-color": "#cccccc",
                                    },
                                )
                            ],
                            width=3,
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col([dcc.Graph(id="highest_directors2")], width=6),
                        dbc.Col([dcc.Graph(id="highest_actors2")], width=6),
                    ]
                ),
            ]
        ),
        label="Movie",
        activeTabClassName="fw-bold",
        label_style={"color": MOV_COLOR},
    )

    @app.callback(
        Output(component_id="highest_actors1", component_property="figure"),
        Output(component_id="highest_directors1", component_property="figure"),
        Input(component_id="dropdown_country1", component_property="value"),
    )
    def actors_directors_show(country):
        return actors_with_most_content.actors_with_most_content(
            country, "TV Show"
        ), directors_with_most_content.directors_with_most_content(country, "TV Show")

    @app.callback(
        Output(component_id="highest_actors2", component_property="figure"),
        Output(component_id="highest_directors2", component_property="figure"),
        Input(component_id="dropdown_country2", component_property="value"),
    )
    def actors_directors_movie(country):
        return actors_with_most_content.actors_with_most_content(
            country, "Movie"
        ), directors_with_most_content.directors_with_most_content(country, "Movie")

    return dbc.Tabs([country_actors_tab_show, country_actors_tab_movie])
