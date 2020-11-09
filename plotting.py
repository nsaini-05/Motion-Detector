from Script import df

from bokeh.plotting import figure , output_file,show
from bokeh.models import Range1d
from bokeh.models import HoverTool
from bokeh.models import ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")




cds = ColumnDataSource(df)

p = figure(title = "19" , x_axis_type= "datetime" , height = 500 , width = 500 )
p.xaxis.axis_label = "Times"


p.y_range=Range1d(0, 1)
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

hover = HoverTool(tooltips=[("Start","@Start_string") , ("End","@End_string")])
p.add_tools(hover)



q = p.quad(left = "Start" , right = "End" , bottom = 0 , top= 0.5 , color= "red" , source =cds)

output_file("Graph.html")
show(p)
