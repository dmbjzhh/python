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

L=len(data['links'])
Edges=[(data['links'][k]['source'], data['links'][k]['target']) for k in range(L)]

G=ig.Graph(Edges, directed=False)

labels=[]
group=[]
for node in data['nodes']:
    labels.append(node['name'])
    group.append(node['group'])

layt=G.layout('kk', dim=3)

Xn=[layt[k][0] for k in range(N)]# 节点的x坐标
Yn=[layt[k][1] for k in range(N)]# 节点的y坐标
Zn=[layt[k][2] for k in range(N)]# 节点的z坐标
Xe=[]
Ye=[]
Ze=[]
for e in Edges:
    Xe+=[layt[e[0]][0],layt[e[1]][0], None] # 边缘的x坐标
    Ye+=[layt[e[0]][1],layt[e[1]][1], None]
    Ze+=[layt[e[0]][2],layt[e[1]][2], None]

axis=dict(
    showbackground=False,
    showline=False,
    zeroline=False,
    showgrid=False,
    showticklabels=False,
    title=''
)

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
                    line = {'width':1, 'color': 'rgb(125, 125, 125)'},
                    #line=Line(color='rgb(125,125,125)', width=1),
                    hoverinfo='none'
                ),
                go.Scatter3d(
                    x=Xn,
                    y=Yn,
                    z=Zn,
                    mode='markers',
                    name='actors',
                    marker = {
                        'size':6,
                        'line':{'width':0.5, 'color': 'rgb(50,50,50)'},
                        'color':'group',
                        'colorscale': 'Viridis'
                    },
                    
                    text=labels,
                    hoverinfo='text'
                )
            ],
            'layout':go.Layout(
                title="Network of coappearances of characters in Victor Hugo's novel<br> Les Miserables (3D visualization)",
                width=1000,
                height=1000,
                showlegend=True,
                # scene={
                #     'xaxis':XAxis(axis),
                #     'yaxis':YAxis(axis),
                #     'zaxis':ZAxis(axis),
                # },
                margin = {'l' : 40, 'b' : 40, 't' : 10, 'r' : 10},
                hovermode='closest',
                annotations = [{
                    'showarrow':False,
                    'text':"Data source: lala",
                    'xref':'paper',
                    'yref':'paper',
                    'x':0,
                    'y':0.1,
                    'xanchor':'left',
                    'yanchor':'bottom',
                    'font':{'size':14}
                }]
            )
        }

    )
])

if __name__ == '__main__':
    app.run_server()