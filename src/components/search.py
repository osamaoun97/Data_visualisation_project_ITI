from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from ..graphs import search_items
from const import *

df = df.copy(deep=True)


def search_box(app):
    @app.callback(
        Output(component_id="names", component_property="options"),
        Input(component_id="radio_search", component_property="value"),
    )
    def items_callback(value):
        return list(df["title"][df["type"] == value])

    @app.callback(
        Output(component_id="Genre", component_property="children"),
        Output(component_id="Directors", component_property="children"),
        Output(component_id="country", component_property="children"),
        Output(component_id="Release_year", component_property="children"),
        Output(component_id="Duration", component_property="children"),
        Output(component_id="desc", component_property="children"),
        Input(component_id="button1", component_property="n_clicks"),
        State(component_id="radio_search", component_property="value"),
        State(component_id="names", component_property="value"),
    )
    def search_callback(n_clicks, type_, title):
        return search_items.fetch_item(type_, title)

    return html.Div(
        [
            dbc.Button(
                "Open Search Tab",
                id="open-offcanvas",
                color="secondary",
                size="sm",
                className="me-md-2",
            ),
        ],
    )
