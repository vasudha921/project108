import plotly.figure_factory as ff
import pandas as pd
import plotly_express as px

df = pd.read_csv("distributerating.csv")
fig = ff.create_distplot([df["Avg Rating"]], ["Rating plotting"])
fig.show()

fig2 = px.scatter(df, x = "Avg Rating", title = "rating plotting")
fig2.show()