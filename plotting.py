# hack-jaipur
# hack jaipur submission repository
# Team Name : TechStars

from main import df
from bokeh.plotting import  figure, show, output_file
from bokeh.models import HoverTool , ColumnDataSource

from playsound import playsound
playsound('audio.mp3')


df["Start_string"]=df["Start"].dt.strftime("%H:%M:%S %D-%M-%Y")
df["End_string"]=df["End"].dt.strftime("%H:%M:%S %D-%M-%Y")


cds=ColumnDataSource(df)

p=figure(x_axis_type='datetime',height=300, width=700,title="Motion Graph")
p.yaxis.minor_tick_line_color=None
# p.ygrid[0].ticker.desired_num_ticks=1

hover=HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
p.add_tools(hover)

q=p.quad(left="Start",right="End",bottom=0,top=1,color="orange",source=cds)

output_file=("Log.html")

show(p)