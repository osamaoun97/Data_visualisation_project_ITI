from ..graphs import dist_of_length, show_longest_by_type
import dash_bootstrap_components as dbc
from dash import dcc
from const import *


def dist_longest_tabs(app):
    dist_longest_show_tab = dbc.Tab(
        dbc.Card(
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    dcc.Graph(
                                        figure=dist_of_length.dist_of_length("TV Show"),
                                        id="distribution_length1",
                                    )
                                ],
                                width=6,
                            ),
                            dbc.Col(
                                [
                                    dcc.Graph(
                                        figure=show_longest_by_type.show_longest_by_type(
                                            "TV Show"
                                        ),
                                        id="longest shows/movies1",
                                    )
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

    dist_longest_movie_tab = dbc.Tab(
            dbc.Card(
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dcc.Graph(
                                            figure=dist_of_length.dist_of_length(
                                                "Movie"
                                            ),
                                            id="distribution_length2",
                                        )
                                    ],
                                    width=6,
                                ),
                                dbc.Col(
                                    [
                                        dcc.Graph(
                                            figure=show_longest_by_type.show_longest_by_type(
                                                "Movie"
                                            ),
                                            id="longest shows/movies2",
                                        )
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

    return dbc.Tabs([dist_longest_show_tab, dist_longest_movie_tab])
