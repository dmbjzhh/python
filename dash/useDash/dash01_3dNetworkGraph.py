# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

app = dash.Dash()

app.layout = html.Div([
    html.H1(
        'Memory Presentation',
        style = {
            'textAlign': 'center'
        }
    ),

    html.Div(
        '3D network graph',
        style = {
            'textAlign': 'center'
        }
    ),
    
    html.Div([
        html.Button(
            'prev',
            id = 'prev-button',
            style = {
                'float': 'left'
            }
        ),
        html.Button(
            'next',
            id = 'next-button',
            style = {
                'float': 'left'
            }
        )
    ]),

    dcc.Graph(
        id = 'network-graph'

    ),

    html.Pre(
        id = 'node-content'
    )
])

if __name__ == '__main__':
    app.run_server()