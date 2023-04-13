
import dash_bootstrap_components as dbc
from dash import Dash
from src.components.layout import create_layout

def main() -> None:
    app = Dash(external_stylesheets=[dbc.themes.DARKLY], title="Netflix Dashboard")
    server = app.server

    app.layout = create_layout(app)
    app.run()


main()