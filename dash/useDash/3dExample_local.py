# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import json
import igraph as ig

app = dash.Dash()

data = []

# 读取json文件放到data数组中

with open("E:/python_git/python/dash/useDash/json/3dexample.json","r") as f:
    data = json.loads(f.read())

N=len(data['nodes'])

# L = 254
L=len(data['links'])
# Edges是一个长度为254数组，数组的元素是元组，元组是source和target的元组对
Edges=[(data['links'][k]['source'], data['links'][k]['target']) for k in range(L)]

# 只有数字，顶点名称或igraph.Vertex对象可以转换为顶点ID
G=ig.Graph(Edges, directed=False)

labels=[]
group=[]
for node in data['nodes']:
    labels.append(node['name'])
    group.append(node['group'])

# 具有77个顶点和3维布局
layt=G.layout('kk', dim=3)

Xn=[layt[k][0] for k in range(N)]# 节点的x坐标
Yn=[layt[k][1] for k in range(N)]# 节点的y坐标
Zn=[layt[k][2] for k in range(N)]# 节点的z坐标
Xe=[]
Ye=[]
Ze=[]
for e in Edges:
    Xe+=[layt[e[0]][0],layt[e[1]][0], None] # 边的x坐标
    Ye+=[layt[e[0]][1],layt[e[1]][1], None]
    Ze+=[layt[e[0]][2],layt[e[1]][2], None]

axis={
    'showbackground':False,
    'showline':False,
    'zeroline':False,
    'showgrid':False,
    'showticklabels':False,
    'title':''    # 标题，默认显示在坐标轴的终点
}

app.layout = html.Div([
     dcc.Graph(
        id = 'network-graph',
        figure = {
            'data':[
                go.Scatter3d(
                    x=Xe,
                    y=Ye,
                    z=Ze,
                    mode='lines',
                    line = {'width':1, 'color': 'rgb(125, 125, 125)'},    # 散点中间连接的线条是灰色，宽度是1px
                    hoverinfo='none'
                ),
                go.Scatter3d(
                    x=Xn,
                    y=Yn,
                    z=Zn,
                    mode='markers+text',    # marker属性是只显示散点，不显示它的说明文字，marker+text两者都显示，文字显示位置可用textposition控制
                    name='actors',    # name会在鼠标悬停时显示在出现的框的外面的右边
                    marker = {
                        'size':6,    # 散点大小
                        'line':{'width':0.5, 'color': 'rgb(50,50,50)'},    # 线条是深灰色
                        'symbol': 'circle',    # 控制散点的形状，circle是圆形，circle-open是里面的不带颜色的
                        'color': group,    # 给散点颜色分类的，否则颜色都一样
                        'colorscale': 'Portland',    # 控制散点的色彩范围
                    },
                    text=labels,    # 与每个坐标相关联的文本，如果设置了hoverinfo，且没设置hovertext时，这些文本会被显示；如果没设置hoverinfo，会直接接着显示在悬浮框里
                    # hoverinfo='text'
                )
            ],
            'layout':go.Layout(
                title="Network of coappearances of characters in Victor Hugo's novel<br> Les Miserables (3D visualization)",
                width=1000,
                height=1000,
                showlegend=False,    # 决定是否在右上角显示哪条线对应什么，哪个点对应什么，默认为true，
                scene={    # 设置此轨迹的3D坐标系和3D场景之间的引用
                    'xaxis': axis,
                    'yaxis': axis,
                    'zaxis': axis
                },
                margin = {'l' : 100, 'b' : 100, 't' : 100, 'r' : 100},    # 控制Graph离网页边缘的距离
                hovermode='closest',    # 确定此场景的悬停交互模式，有两个值，一个是closest，一个是False，
                annotations = [{    # 注解，它是一个文本元素，可以放置在图形的任何地方，它可以根据图中的相对坐标或相对于图的实际数据坐标来定位，它可以显示为有或没有箭头
                    'showarrow':False,    # 确定注释是否用箭头绘制。如果true，文本放在箭头的尾部附近；如果False，text与提供的x和y对齐
                    'text':"Data source: lala",    # 设置与此注释关联的文本
                    'xref':'paper',    # 设置注释的x坐标轴
                    'yref':'paper',
                    'x':0,    # 设置注释的x位置
                    'y':0.1,
                    'xanchor':'left',    # 设置文本框的水平位置
                    'yanchor':'bottom',
                    'font':{'size':14}
                }]
            )
        }

    )
])

if __name__ == '__main__':
    app.run_server()