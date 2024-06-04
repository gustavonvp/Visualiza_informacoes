import plotly.express as px
import pandas as pd

data = pd.read_csv("C:/Users/usuario/Downloads/co2-fossil-plus-land-use.csv")

df = px.data.gapminder().query("year==2007")
# Generate scatter geo graph
fig = px.scatter_geo(df, locations="iso_alpha", color='continent',
                     hover_name="country", size="pop",
                     animation_frame="year",
                     projection='satellite')
fig.show()