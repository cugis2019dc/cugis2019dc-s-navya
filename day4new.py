import pandas as pd
dir(pandas)
import plotly
import plotly.graph_objs as go


wodf = pd.read_excel("GISdata.xlsx", sheet_name = "womenOccupation")
wodf

titles = go.Layout (title = "Percentage of Women Employed by Occupation",
                    xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Occupation",)),
                    yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Percentage",))
)


wodf = pd.read_excel("GISdata.xlsx", sheet_name = "womenOccupation")
                     
womenoccupation=go.Bar(x=wodf["occupation"],y=wodf["women"],
                       marker = {"color": wodf["women"], "colorscale" : "tealrose"}) #tell python which element needs color


fig = go.Figure(data= [womenoccupation], layout=titles)
plot(fig)

