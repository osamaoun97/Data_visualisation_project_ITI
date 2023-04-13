from dash import html
import dash_bootstrap_components as dbc
from . import (
    search,
    logo,
    country_month,
    bans,
    directors_actors,
    dist_longest,
    footer,
    off_canvas,
    rating_year,
    search,
    treemap_genre,
)


def create_layout(app):
    return html.Div(
        dbc.Container(
            [
                search.search_box(app),
                html.Br(),
                logo.logo(app),
                html.Br(),
                bans.bans(app),
                html.Br(),
                off_canvas.off_canvas(app),
                html.Br(),
                rating_year.rating_year(app),
                html.Br(),
                country_month.country_month_tabs(app),
                html.Br(),
                dist_longest.dist_longest_tabs(app),
                html.Br(),
                treemap_genre.treemap_elem(app),
                html.Br(),
                directors_actors.directors_actors_tabs(app),
                footer.footer(app)
            ]
        ),
        style={"background-color": "#111111"},
    )
