import dash
import dash_html_components as html
import dash_core_components as dcc
import os

from flask import send_from_directory

app = dash.Dash()

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = html.Div([

    html.Link(
        rel='stylesheet',
        href='static/stylesheet.css' # E:/python_git/python/dash/useDash/
    ),

    html.Div('Hello world'),

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
])


@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)


if __name__ == '__main__':
    app.run_server(debug=True)