from dash import Dash, dcc, html, dash_table, Input, Output, State, callback
import dash_bootstrap_components as dbc
import base64
import datetime
import io
import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash.dependencies import Input, Output
import dash_core_components as dcc
from app import app

# dash_app = dash.Dash(__name__, server=app, routes_pathname_prefix='/dashboard/')

def create_dashboard(flask_app):
    dash_app = dash.Dash(
        __name__,
        server=flask_app,
        routes_pathname_prefix='/dashboard/'
    )


# Aquí configuras el layout de Dash
dash_app.layout = html.Div([

    html.H1("Bienvenido al Dashboard"),
    html.Div(id="user-info"),
    # Aquí agregarías más componentes de Dash (gráficos, tablas, etc.)
])



# Callback para mostrar el token o cualquier otra información
# @dash_app.callback(
#     Output('user-info', 'children'),
#     Input('user-token', 'data')
# )
# def display_user_info(data):
#     token = data.get('token', 'No disponible')
#     return f'Token de usuario: {token}'
# @dash_app.callback(
#     Output('user-info', 'children'),
#     Input('user-token', 'data')
# )
# def display_user_info(data):
#     if data:
#         token = data.get('token', 'No disponible')
#         return f'Token de usuario: {token}'
#     return 'No hay datos disponibles'

