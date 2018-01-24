# -*- coding: utf-8 -*-

# 根据大陆来分类，以gdp为横轴，LifeExpectancy为纵轴


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
    'gdp-life-exp-2007.csv')

app.layout = html.Div([
    dcc.Graph(
        id = 'life-exp-vs-gdp',
        figure = {
            'data' : [
                go.Scatter(    #scatter plot散点图
                    x = df[df['continent'] == i]['gdp per capita'],    # 鼠标划过时，显示框里的x轴坐标
                    y = df[df['continent'] == i]['life expectancy'],    # 鼠标滑过时，显示框里的y轴坐标
                    text = df[df['continent'] == i]['country'],    # 鼠标滑过时，显示的框里的文本
                    mode = 'markers',
                    opacity = 0.7,    # opacity是每个散点的透明度
                    marker = {    # marker就是每条数据对应的散点
                        'size' : 15,    # size是每个散点的大小
                        'line' : {'width' : 0.5, 'color' : 'white'}    # line是散点的边框
                    },
                    name = i    # 鼠标滑过显示的文本框的名字，显示在框外的右边
                ) for i in df.continent.unique()
            ],
            'layout' : go.Layout(
                xaxis = {'type' : 'log', 'title' : 'GDP per Capita'},
                yaxis = {'title' : 'Life Expectancy'},
                margin = {'l' : 40, 'b' : 40, 't' : 10, 'r' : 10},    # 这个graph距离网页的边框大小，l是左边，距左边40px
                hovermode = 'closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()