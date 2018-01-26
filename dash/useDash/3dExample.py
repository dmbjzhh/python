# -*- coding: utf-8 -*-

import igraph as ig
# 将图形定义为igraph.Graph对象，从json文件中读取图形对象数据
import json
import urllib2

import plotly.plotly as py
from plotly.graph_objs import *

import plotly

plotly.tools.set_credentials_file(username='dmbjzhh', api_key='PLUgUfiM4uDCSpOw66Yb')

data = []
req = urllib2.Request("https://raw.githubusercontent.com/plotly/datasets/master/miserables.json")
opener = urllib2.build_opener()
f = opener.open(req)
data = json.loads(f.read())

# print data.keys()得到 [u'nodes', u'links']

# 获取节点的数目
N=len(data['nodes'])
# N等于77

# 定义边的列表和来自边的Graph对象
L=len(data['links'])
Edges=[(data['links'][k]['source'], data['links'][k]['target']) for k in range(L)]

G=ig.Graph(Edges, directed=False)

# 提取节点的属性： 'group'和 'name'
# data['nodes'][0] 得到 {u'group': 1, u'name': u'Myriel'}
labels=[]
group=[]
for node in data['nodes']:
    labels.append(node['name'])
    group.append(node['group'])

# 获取节点位置，由3D图形的Kamada-Kawai布局设置
layt=G.layout('kk', dim=3)

# layt是三个元素的列表（节点的坐标）
# layt[5]等于[2.4324289406052806, -2.8362864661827363, -3.4528174775780536]

# 为Ploty绘制图形设置数据

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

trace1=Scatter3d(
    x=Xe,
    y=Ye,
    z=Ze,
    mode='lines',
    line=Line(color='rgb(125,125,125)', width=1),
    hoverinfo='none'
)
trace2=Scatter3d(
    x=Xn,
    y=Yn,
    z=Zn,
    mode='markers+text',
    name='actors',
    marker=Marker(
        symbol='dot',
        size=6,
        color=group,
        colorscale='Portland',
        line=Line(color='rgb(50,50,50)', width=0.5)
    ),
    text=labels,
    # hoverinfo='text'
)

axis=dict(
    showbackground=False,
    showline=False,
    zeroline=False,
    showgrid=False,
    showticklabels=False,
    title=''
)

layout = Layout(
    title="Network of coappearances of characters in Victor Hugo's novel<br> Les Miserables (3D visualization)",
    width=1000,
    height=1000,
    showlegend=False,
    scene=Scene(
        xaxis=XAxis(axis),
        yaxis=YAxis(axis),
        zaxis=ZAxis(axis),
    ),
    margin=Margin(
        t=100
    ),
    hovermode=False,
    annotations=Annotations([
        Annotation(
            showarrow=False,
            text="Data source: <a href='http://bost.ocks.org/mike/miserables/miserables.json'>[1] miserables.json</a>",
            xref='paper',
            yref='paper',
            x=0,
            y=0.1,
            xanchor='left',
            yanchor='bottom',
            font=Font(
                size=14
            )
        )
    ])
)

data=Data([trace1, trace2])
fig=Figure(data=data, layout=layout)

py.iplot(fig, filename='Les-Miserables')