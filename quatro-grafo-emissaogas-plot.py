import plotly.express as px
import pandas as pd
import dash
from dash import Dash, html, dcc
from numpy import abs

df = pd.read_csv("C:/Users/usuario/Downloads/Emissions Data.csv")

colors = {
    'background': '#F0F8FF',
    'text': '#00008B'
}
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app = dash.Dash(external_stylesheets=external_stylesheets)

# Plot the scatterplot using Plotly. We ploy y vs x (#Confirmed vs Date)
fig = px.scatter(df, x='Ano', y='Paises', color='Emissao')
fig.update_layout(bargap=1)

app.layout = html.Div(children=[
    html.H1(children='Emissao de gases em toneladas'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

fig.show()

#if __name__ == '__main__':
 #   app.run_server(debug=True, port=8056)