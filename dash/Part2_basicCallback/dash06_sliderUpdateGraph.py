# -*- coding: utf-8 -*-

# 将csv文件中的数据可视化为散点图，并且可以根据底下年份的slider来查看不同的数据

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/'
    'datasets/master/gapminderDataFiveYear.csv')

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id = 'graph-with-slider'),
    dcc.Slider(
        id = 'year-slider',
        min = df['year'].min(),
        max = df['year'].max(),
        value = df['year'].min(),    # 初始值为最小的年份
        step = None,
        marks = {str(year) : str(year) for year in df['year'].unique()}    # slider的点，不同的年份对应不同的点
    )
])

@app.callback(
    dash.dependencies.Output('graph-with-slider', 'figure'),    # 省略了component_id和component_property这两个关键字
    [dash.dependencies.Input('year-slider', 'value')]
)
def update_figure(selected_year):    # callback函数
    filtered_df = df[df.year == selected_year]
    traces = []
    for i in filtered_df.continent.unique():
        df_by_continent = filtered_df[filtered_df['continent'] == i]
        traces.append(go.Scatter(
            x = df_by_continent['gdpPercap'],
            y = df_by_continent['lifeExp'],
            text = df_by_continent['country'],
            mode = 'markers',
            opacity = 0.7,
            marker = {
                'size' : 15,
                'line' : {'width': 0.5, 'color': 'white'}
            },
            name = i
        ))
    
    return {
        'data' : traces,
        'layout' : go.Layout(
            xaxis = {'type' : 'log', 'title' : 'GDP Per Capita'},
            yaxis = {'title' : 'Life Expectancy', 'range' : [20, 90]},
            margin = {'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend = {'x': 0, 'y': 1},
            hovermode = 'closest'
        )
    }

if __name__ == '__main__':
    app.run_server()
