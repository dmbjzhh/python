
关于Dash库：

可以生成交互式web可视化界面

* **安装**：

  ```
  pip install dash==0.19.0  # dash的核心后端
  pip install dash-renderer==0.11.1  # dash的前端
  pip install dash-html-components==0.8.0  # HTML组件
  pip install dash-core-components==0.15.2  # Supercharged components
  pip install plotly --upgrade  # 例子中使用的图形库
  ```

* **用Dash生成HTML**

  Dash应用由两部分组成

  * 第一部分为布局(layout)，描述程序的外观
  * 第二部分描述程序的交互性

  Dash为程序的所有可视化组件都提供了Python类，它们在dash\_core\_components和dash\_html\_components库中，也可以使用JavaScript和React.js构建自己的组件

  其中dash\_html\_components库对每一个HTML标签都有一个对应的类，对所有HTML参数都有对应的关键字参数

  常见的HTML元素：

  ```
  <div>
      <h1>Hello</h1>
      <div>
          <p>Dash converts Python classes into HTML</p>
          <p>This conversion happens behind the scenes by Dash's JavaScript front-end</p>
      </div>
  </div>
  ```

  转化成dash的python结构：

  ```
  import dash_html_components as html

  html.Div([
      html.H1('Hello Dash'),
      html.Div([
          html.P('Dash converts Python classes into HTML'),
          html.P('This conversion happens behind the scenes by Dash's JavaScript front-end')
      ])
  ])
  ```

  ​

  **dash\_html\_components和HTML属性的区别**：

  1. HTML中的`style`属性是以分号分隔的字符串，dash中可以使用字典
  2. 在dash的style字典中，字典的key是使用驼峰命名法，而不是`style`属性的命名，比如不是`text-align`，而是`textAlign`
  3. Dash中的HTML`class`关键字对应的是`className`
  4. HTML标签对里的内容是通过children关键字参数指定的。按照惯例，这总是第一个参数，可以被忽略
  5. HTML中以像素为单位的样式属性，比如15px，在dash中直接写数字就行，不用包含px单位

  两者区别的例子：

  html：

  ```
  <div style="margin-bottom: 50px; margin-top: 25px;">

      <div style="color: blue; font-size: 14px">
          Example Div
      </div>

      <p class="my-class", id="my-p-element">
          Example P
      </p>
      
  <div>
  ```

  dash:

  ```
  import dash_html_components as html

  html.Div([
      html.Div('Example Div', style={'color': 'blue', 'fontSize': 14}),
      html.P('Example P', className='my-class', id='my-p-element')
  ], style={'marginBottom': 50, 'marginTop': 25})
  ```

  ​

  运行编写好的python代码，在浏览器的地址http:127.0.0.1:8050/中可以看到可视化的效果

  ​

* **用Dash生成表格等**

  Dash可以根据Pandas数据框架等生成表格，主要是通过读取csv文件

  其中dash\_core\_components库中还包含`Graph`组件使用开源的plotly.js JavaScript图形库呈现交互式数据可视化。 Plotly.js支持超过35种图表类型，并可以在向量级SVG和高性能WebGL中呈现图表。

  dash\_core\_components.Graph组件中的figure参数与plotly.py使用的图形参数相同。[plotly.py库具体说明](https://plot.ly/python/)

  调用Graph组件的效果：

  这些图形是交互式和响应式的。将鼠标悬停在点上以查看其值，单击图例项目以切换轨迹，单击并拖动以进行缩放，按住Shift键并单击并拖动以平移。


* **用Dash编写markdown**

  dash\_core\_components还包含一组更高级别的组件，如下拉列表，图表，markdown块等。

  如果对html不熟悉的话可以使用Dash编写markdown，比如：

  ```
  import dash_core_components as dcc

  dcc.Markdown('''
  #### Dash and Markdown

  Dash supports [Markdown](http://commonmark.org/help).

  Markdown is a simple way to write and format text.
  It includes a syntax for things like **bold text** and *italics*,
  [links](http://commonmark.org/help), inline `code` snippets, lists,
  quotes, and more.
  ''')
  ```

  ​


#### 总结

总的来说，Dash app的`layout`是描述该app长什么样子的，`layout`是一个组件的分层树

`dash_html_components`库为所有的HTML标签提供类、用来描述HTML属性(如`style`、`className`和`id`)的关键字参数。

`dash_core_components`库生成更高级别的组件，比如control和graph