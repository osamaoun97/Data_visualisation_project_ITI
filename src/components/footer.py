from datetime import datetime
from dash import html


def footer(app):
    return html.Div(
        [
            html.Small(f"© {datetime.now().year}. Created by: "),
            html.A(
                "Osama Fayez",
                href="https://www.linkedin.com/in/osama-oun/",
                target="_blank",
                style={"color": "#dedede"},
            ),
            ", ",
            html.A(
                "Khaled Ehab",
                href="https://www.linkedin.com/in/aleedo/",
                target="_blank",
                style={"color": "#dedede"},
            ),
            " and ",
            html.A(
                "Mariam Gamal",
                href="https://www.linkedin.com/in/mariam-gamal-50a895145/",
                target="_blank",
                style={"color": "#dedede"},
            ),
        ],
        id="footer",
        style={"text-align": "center", "background-color": "#222222"},
    )
