# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
		Dash: A web application framework for Python.
	'''),

    dcc.Graph(
    	id = 'example-graph',
    	figure={
    		'data':[
    			{'x':[1,2,3], 'y':[4,1,2], 'type':'bar', 'name':'SF'},
    			{'x':[1,2,3], 'y':[2,4,5], 'type':'bar', 'name':u'Montréal'},
    		],
    		'layout':{
    			'title' : 'Dash Data Visualization'
    		}
    	}
    )
])

# __name__是内置变量，用于表示当前模块的名字
# 如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。
# 即，如果模块被导入，__name__ != __main__，就不会运行下面的代码
if __name__ == '__main__':
    app.run_server(debug=True)