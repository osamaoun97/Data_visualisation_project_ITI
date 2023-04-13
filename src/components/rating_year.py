from ..graphs import content_by_rating, content_by_year


def rating_year(app):
    content_by_rating_element = dbc.Col(
        [dcc.Graph(figure=content_by_rating(), id="content_by_rating")], width=6
    )
    content_by_year_element = dbc.Col(
        [dcc.Graph(figure=content_by_year(), id="content_by_year")], width=6
    )
    return dbc.Row([content_by_rating_element, content_by_year_element])
