from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
from bokeh.models import ColumnDataSource, HoverTool
from flask import Flask,render_template
from bokeh.io import curdoc,gridplot
import pandas as pd
import numpy as np
app = Flask(__name__)

@app.route('/')
def bokeh():
    fig = figure(title='Hemoglobin',plot_width=400, plot_height=300, x_axis_type="datetime", responsive = True)
    df = pd.DataFrame.from_dict({'dates': ["1-1-2019", "2-1-2019", "3-1-2019", "4-1-2019", "5-1-2019", "6-1-2019", "7-1-2019", "8-1-2019", "9-1-2019", "10-1-2019"], 
                                'x': [10, 15, 16,17 , 15, 15, 15, 20, 15, 19]})
    df['dates'] = pd.to_datetime(df['dates'])
    source = ColumnDataSource(df)
    fig.line(
        x='dates',
        y='x', 
        source=source,
        line_width=2
    )
    fig.circle(x='dates', y='x',source=source, fill_color="#F8E9A1", size=8)
    fig.add_tools(HoverTool(tooltips=[("Y", "@x")]))
    fig.border_fill_color = "#a8d0e6"
    fig.min_border_right = 80
    s2 = figure(title='Hemoglobin',plot_width=400, plot_height=300, x_axis_type="datetime", responsive = True)
    source = ColumnDataSource(df)
    s2.line(
        x='dates',
        y='x', 
        source=source,
        line_width=2
    )
    s2.circle(x='dates', y='x',source=source, fill_color="#F8E9A1", size=8)
    s2.add_tools(HoverTool(tooltips=[("Y", "@x")]))
    s2.border_fill_color = "#a8d0e6"
    s2.min_border_right = 80
    # create and another
    s3 = figure(title='Hemoglobin',plot_width=400, plot_height=300, x_axis_type="datetime", responsive = True)
    source = ColumnDataSource(df)
    s3.line(
        x='dates',
        y='x', 
        source=source,
        line_width=2
    )
    s3.circle(x='dates', y='x',source=source, fill_color="#F8E9A1", size=8)
    s3.add_tools(HoverTool(tooltips=[("Y", "@x")]))
    s3.border_fill_color = "#a8d0e6"
    s3.min_border_right = 80
    s4 = figure(title='Hemoglobin',plot_width=400, plot_height=300, x_axis_type="datetime", responsive = True)
    source = ColumnDataSource(df)
    s4.line(
        x='dates',
        y='x', 
        source=source,
        line_width=2
    )
    s4.circle(x='dates', y='x',source=source, fill_color="#F8E9A1", size=8)
    s4.add_tools(HoverTool(tooltips=[("Y", "@x")]))
    s4.border_fill_color = "#a8d0e6"
    s4.min_border_right = 80
    s5 = figure(title='Hemoglobin',plot_width=400, plot_height=300, x_axis_type="datetime", responsive = True)
    source = ColumnDataSource(df)
    s5.line(
        x='dates',
        y='x', 
        source=source,
        line_width=2
    )
    s5.circle(x='dates', y='x',source=source, fill_color="#F8E9A1", size=8)
    s5.add_tools(HoverTool(tooltips=[("Y", "@x")]))    
    s5.border_fill_color = "#a8d0e6"
    s5.min_border_right = 80
    s6 = figure(title='Hemoglobin',plot_width=400, plot_height=300, x_axis_type="datetime", responsive = True)
    source = ColumnDataSource(df)
    s6.line(
        x='dates',
        y='x', 
        source=source,
        line_width=2
    )
    s6.circle(x='dates', y='x',source=source, fill_color="#F8E9A1", size=8)
    s6.add_tools(HoverTool(tooltips=[("Y", "@x")]))
    s6.border_fill_color = "#a8d0e6"
    s6.min_border_right = 80
    p = gridplot([[fig, s2,s3],[s4,s5,s6]])
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()
    # render template
    script, div = components(p)
    html = render_template(
        'patients.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return encode_utf8(html)
if __name__ == '__main__':
    app.run(debug=True)