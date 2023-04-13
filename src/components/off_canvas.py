import dash_bootstrap_components as dbc
from dash import dcc
from const import *
from dash import html, Output, Input, State
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc


def off_canvas(app):
    @app.callback(
        Output("offcanvas", "is_open"),
        Input("open-offcanvas", "n_clicks"),
        [State("offcanvas", "is_open")],
    )
    def toggle_offcanvas(n1, is_open):
        if n1:
            return not is_open
        return is_open

    return html.Div(
        [
            dbc.Offcanvas(
                [
                    dbc.Col(
                        dbc.Card(
                            [
                                dcc.RadioItems(
                                    ["TV Show", "Movie"],
                                    "TV Show",
                                    id="radio_search",
                                    inline=True,
                                    labelStyle={
                                        "font-size": "18px",
                                        "color": "#FFFFFF",
                                        "cursor": "pointer",
                                        "margin-left": "20px",
                                    },
                                ),
                                html.Br(),
                                dcc.Dropdown(
                                    list(df["title"].unique()),
                                    value="",
                                    id="names",
                                    placeholder="Select the title",
                                    multi=False,
                                    style={
                                        "color": "#000000",
                                        "background-color": "#cccccc",
                                    },
                                ),
                                html.Br(),
                                dbc.Button("Search", id="button1", color="danger"),
                            ],
                            style={"font-size": "17px"},
                        )
                    ),
                    html.Br(),
                    dbc.Col(
                        dbc.Card(
                            [
                                dmc.Text(
                                    id="Genre",
                                    size="l",
                                    style={
                                        "font-size": "17px",
                                        "fontWeight": "bold",
                                        "color": "#FFFFFF",
                                    },
                                ),
                                html.Br(),
                                dmc.Text(
                                    id="Directors",
                                    size="l",
                                    style={
                                        "font-size": "17px",
                                        "fontWeight": "bold",
                                        "color": "#FFFFFF",
                                    },
                                ),
                                html.Br(),
                                dmc.Text(
                                    id="country",
                                    size="l",
                                    style={
                                        "font-size": "17px",
                                        "fontWeight": "bold",
                                        "color": "#FFFFFF",
                                    },
                                ),
                                html.Br(),
                                dmc.Text(
                                    id="Release_year",
                                    size="l",
                                    style={
                                        "font-size": "17px",
                                        "fontWeight": "bold",
                                        "color": "#FFFFFF",
                                    },
                                ),
                                html.Br(),
                                dmc.Text(
                                    id="Duration",
                                    size="l",
                                    style={
                                        "font-size": "17px",
                                        "fontWeight": "bold",
                                        "color": "#FFFFFF",
                                    },
                                ),
                            ],
                        )
                    ),
                    html.Br(),
                    html.Br(),
                    dbc.Col(
                        [
                            dbc.Card(
                                dmc.Text(
                                    id="desc",
                                    size="l",
                                    style={
                                        "font-size": "17px",
                                        "fontWeight": "bold",
                                        "color": "#FFFFFF",
                                    },
                                )
                            )
                        ]
                    ),
                ],
                id="offcanvas",
                title="Search by Title",
                is_open=False,
                style={"background-color": "#222222"},
            ),
        ]
    )
