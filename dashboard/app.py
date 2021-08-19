import dash
import dash_bootstrap_components as dbc
import flask

FA = "https://use.fontawesome.com/releases/v5.15.1/css/all.css"

server = flask.Flask(__name__)
dash_app = dash.Dash(
    __name__,
    server=server,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP, FA],
    eager_loading=True,
    update_title='Loading...',
    title='Crypto Portfolio Monitor'
)
