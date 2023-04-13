from ..graphs import production_by_month, production_by_country
import dash_bootstrap_components as dbc
from dash import dcc
from const import *
from dash import html


def country_month_tabs(app):
    production_country_month_tab_show = dbc.Tab(
        dbc.Card(
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    dcc.Graph(
                                        figure=production_by_country.production_by_country(
                                            "TV Show"
                                        ),
                                        id="production_by_country1",
                                    )
                                ],
                                width=6,
                            ),
                            dbc.Col(
                                [
                                    dcc.Graph(
                                        figure=production_by_month.production_by_month(
                                            "TV Show"
                                        ),
                                        id="production_by_month1",
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

    production_country_month_tab_movie = dbc.Tab(
        dbc.Card(
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    dcc.Graph(
                                        figure=production_by_country.production_by_country(
                                            "Movie"
                                        ),
                                        id="production_by_country2",
                                    )
                                ],
                                width=6,
                            ),
                            dbc.Col(
                                [
                                    dcc.Graph(
                                        figure=production_by_month.production_by_month(
                                            "Movie"
                                        ),
                                        id="production_by_month2",
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

    return dbc.Tabs(
        [production_country_month_tab_show, production_country_month_tab_movie]
    )
