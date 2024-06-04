import plotly.express as px
import pandas as pd

df = pd.read_csv("C:/Users/usuario/Downloads/Emissions Data.csv")

# Plot the scatterplot using Plotly. We ploy y vs x (#Confirmed vs Date)
fig = px.scatter(df, x='Ano', y='Paises', color='Emissao')
fig.update_traces(mode='markers+lines')
fig.show()
