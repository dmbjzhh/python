# -*- coding:utf-8 -*-

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='input1', type='text', value='init'),
    html.Button('Shaw', id = 'button1', n_clicks = 0)
])

count = 0

@app.callback(
    Output('input1', 'value'),
    [Input('button1', 'n_clicks')]
)
def update(n_clicks):
    if n_clicks == 0:
        return None
    global count
    count += 1
    return 'you click {} times.'.format(count)

if __name__ == '__main__':
    app.run_server()