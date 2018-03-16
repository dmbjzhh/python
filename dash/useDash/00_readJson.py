# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import os,sys

print os.path.abspath('.')
print sys.path[0]

json_path = os.path.join(sys.path[0], 'json')

print json_path

# 一种输出当前目录下所有文件的方法
def file_name(file_dir):   
    for root, dirs, files in os.walk(file_dir):  
        print(root) #当前目录路径  
        print(dirs) #当前路径下所有子目录  
        print(files) #当前路径下所有非目录子文件

json_files = os.listdir(json_path)

json_files_num = len(json_files)

app = dash.Dash()
app.layout = html.Div([
    dcc.Slider(
        id='my-slider',
        min=0,
        max=json_files_num,
        marks={i: 'State {}'.format(i) for i in range(json_files_num)},
        value=0,
    ),
    html.Div(id='slider-output-container', style = {'marginTop': 20})
],style = { 'width':800, 'float': 'left'})


@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server()