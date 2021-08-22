import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Input import Input
import dash_html_components as html
from dash_html_components.Button import Button
from dash_html_components.Col import Col
import dash_core_components as dcc
from dash_html_components.Output import Output
import dash

login_box = html.Div(
    [
        html.Div(
            [
                html.Div("Sign In", className="active", id="login-button", n_clicks=0),
                html.Div("Sign Up", id="signup-button", n_clicks=0),
            ],
            className="tab-header",
        ),
        html.Hr(),
        html.Div(
            [
                html.Div(
                    [
                        html.Form(
                            [
                                dbc.Input(id="username-input", placeholder="Username or email", type="text", bs_size="sm", className="form-element"),
                                dbc.Input(id="password-input", placeholder="Password", type="password", bs_size="sm", className="form-element"),
                                dbc.Button("Log In", className="button"),
                                html.Hr(),
                                html.P("Forgot password?",
                                style = {
                                    "margin": 0,
                                    "text-align": "center",
                                    "margin-top": "1rem",
                                    "cursor": "pointer",
                                    "-webkit-user-select": "none",
                                    "-khtml-user-select": "none",
                                    "-moz-user-select": "-moz-none",
                                    "-o-user-select": "none",
                                    "user-select": "none",
                                }
                                )
                            ],
                            className="form-elements",
                        ),
                    ],
                    className="tab-body active",
                    id="log-body"
                ),
                html.Div(
                    [
                        html.Form(
                            [
                                dbc.Input(id="username-input", placeholder="Username", type="text", bs_size="sm", className="form-element"),
                                dbc.Input(id="username-input", placeholder="Email", type="text", bs_size="sm", className="form-element"),
                                dbc.Input(id="password-input", placeholder="Password", type="password", bs_size="sm", className="form-element"),
                                dbc.Input(id="password-input", placeholder="Repeat password", type="password", bs_size="sm", className="form-element"),
                                dbc.Button("Sign Up", className="button"),
                            ],
                            className="form-elements",
                        ),
                    ],
                    className="tab-body",
                    id="reg-body"
                ),
            ],
            className="tab-content"
        ), 
    ],
    className="form",
)


login_layout = html.Div(
    [
        login_box,
    ],
    className="layout",
)




