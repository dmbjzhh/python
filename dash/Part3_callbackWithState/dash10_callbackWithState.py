# -*- coding: utf-8 -*-

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value='ace'),
    dcc.Input(id='input-2-state', type='text', value='song'),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-state')
])

@app.callback(
    Output('output-state', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('input-1-state', 'value'),
     State('input-2-state', 'value')]
)
def update_output(n_clicks, input1, input2):
    return u'''
        The Button has been Pressed {} times,
        Input 1 is "{}",
        Input 2 is "{}"
    '''.format(n_clicks, input1, input2)

if __name__ == '__main__':
    app.run_server(debug=True)
