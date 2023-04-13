from ..graphs import treemap
from ..graphs.genre_by_year import genre_by_year
import dash_bootstrap_components as dbc
from const import *
from dash_bootstrap_templates import load_figure_template

load_figure_template("DARKLY")
from dash import Dash, html, dcc, Input, Output, State


def treemap_elem(app):
    @app.callback(
        Output(component_id="genre_by_year_movies", component_property="figure"),
        Input(component_id="genres_option_movie", component_property="value"),
    )
    def genre_by_year_movie(genre):
        return genre_by_year(genre, "Movie")

    @app.callback(
        Output(component_id="genre_by_year_shows", component_property="figure"),
        Input(component_id="genres_options_tv_show", component_property="value"),
    )
    def genre_by_year_show(genre):
        return genre_by_year(genre, "TV Show")

    treemap_genre_tab_show = dbc.Tab(
        dbc.Card(
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                dcc.Graph(
                                    figure=treemap.treemap_graph("TV Show"),
                                    id="treemap1",
                                ),
                                width=6,
                            ),
                            dbc.Col(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                html.Small(
                                                    "Select the genre: ",
                                                    style={
                                                        "font-size": "18px",
                                                        "font-weight": "bold",
                                                    },
                                                ),
                                                width=3,
                                            ),
                                            dbc.Col(
                                                dcc.Dropdown(
                                                    GENRES_SHOWS,
                                                    value="TV Dramas",
                                                    id="genres_options_tv_show",
                                                    placeholder="Select a genre",
                                                    multi=False,
                                                    style={
                                                        "color": "#000000",
                                                        "background-color": "#cccccc",
                                                    },
                                                ),
                                                width=6,
                                            ),
                                        ]
                                    ),
                                    dcc.Graph(id="genre_by_year_shows"),
                                ],
                                width=6,
                            ),
                        ]
                    )
                ]
            ),
            className="mt-3",
        ),
        label="TV Show",
        activeTabClassName="fw-bold",
        label_style={"color": "#E50914"},
    )

    treemap_genre_tab_movie = dbc.Tab(
        dbc.Card(
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                dcc.Graph(
                                    figure=treemap.treemap_graph("Movie"),
                                    id="treemap2",
                                ),
                                width=6,
                            ),
                            dbc.Col(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                html.Small(
                                                    "Select the genre: ",
                                                    style={
                                                        "font-size": "18px",
                                                        "font-weight": "bold",
                                                    },
                                                ),
                                                width=3,
                                            ),
                                            dbc.Col(
                                                dcc.Dropdown(
                                                    GENRES_MOVIES,
                                                    value="Dramas",
                                                    id="genres_option_movie",
                                                    placeholder="Select a genre",
                                                    multi=False,
                                                    style={
                                                        "color": "#000000",
                                                        "background-color": "#cccccc",
                                                    },
                                                ),
                                                width=6,
                                            ),
                                        ]
                                    ),
                                    dcc.Graph(id="genre_by_year_movies"),
                                ],
                                width=6,
                            ),
                        ]
                    )
                ]
            ),
            className="mt-3",
        ),
        label="Movie",
        activeTabClassName="fw-bold",
        label_style={"color": MOV_COLOR},
    )

    return dbc.Tabs([treemap_genre_tab_show, treemap_genre_tab_movie])
