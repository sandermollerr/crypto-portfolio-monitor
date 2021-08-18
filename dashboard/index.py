import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input
from dash.dependencies import Output
from dash.dependencies import State

from dashboard.app import dash_app

navbar = dbc.NavbarSimple(
    children=[
        dbc.Button("Sidebar", outline=True, color="secondary", className="mr-1", id="btn_sidebar"),
        dbc.Button("Crypto portfolio monitor", outline=True, color="secondary", className="mr-1", id="btn_nav_title", href='/'),
    ],
    color="dark",
    dark=True,
    fluid=True,
)

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 62.5,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0.5rem 1rem",
    "background-color": "#f8f9fa",
}

SIDEBAR_HIDEN = {
    "position": "fixed",
    "top": 62.5,
    "left": "-16rem",
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0rem 0rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "transition": "margin-left .5s",
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE1 = {
    "transition": "margin-left .5s",
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

sidebar_nav_links = [
    'Overview',
    'Coinbase',
    'Kraken'
]

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-5"),
        html.Hr(),
        dbc.Nav(
            [
                *[dbc.NavLink(nav_name, href=f"/{nav_name.lower()}", id=f"{nav_name.lower()}-screen-link") for nav_name in
                  sidebar_nav_links]
            ],
            vertical=True,
            pills=True,
        ),
    ],
    id="sidebar",
    style=SIDEBAR_STYLE,
)

content = html.Div(

    id="page-content",
    style=CONTENT_STYLE)

dash_app.layout = html.Div(
    [
        dcc.Store(id='side_click'),
        dcc.Location(id="url"),
        navbar,
        sidebar,
        content,
    ],
)


@dash_app.callback(
    [
        Output("sidebar", "style"),
        Output("page-content", "style"),
        Output("side_click", "data"),
    ],

    [Input("btn_sidebar", "n_clicks")],
    [
        State("side_click", "data"),
    ]
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = SIDEBAR_HIDEN
            content_style = CONTENT_STYLE1
            cur_nclick = "HIDDEN"
        else:
            sidebar_style = SIDEBAR_STYLE
            content_style = CONTENT_STYLE
            cur_nclick = "SHOW"
    else:
        sidebar_style = SIDEBAR_STYLE
        content_style = CONTENT_STYLE
        cur_nclick = 'SHOW'

    return sidebar_style, content_style, cur_nclick


@dash_app.callback(
    [Output(f"overview-screen-link", "active"),
     Output(f"coinbase-screen-link", "active"),
     Output(f"kraken-screen-link", "active")],
    [Input("url", "pathname")],
)
def toggle_active_sidebar_links(pathname):
    if pathname in ["/", "/overview"]:
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/{nav_name.lower()}" for nav_name in sidebar_nav_links]


@dash_app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname in ["/", "/overview"]:
        return html.P("Overview page")
    elif pathname == "/coinbase":
        return html.P("Coinbase page")
    elif pathname == "/kraken":
        return html.P("Kraken page")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == '__main__':
    dash_app.run_server(debug=True, port=8000, host='0.0.0.0')
