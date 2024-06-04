
from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px

#df = pd.DataFrame()
df = pd.read_csv("dados/life-expectancy.csv", index_col=0)

fig = px.histogram(df,  x="Code", y="Life expectancy (years)", histfunc='count', nbins=50)
fig.update_layout(bargap=0.2)

fig2 = px.histogram(df, x="Code", y="Life expectancy (years)", histfunc='sum')
fig2.update_layout(bargap=0.2)

fig3 = px.histogram(df, x="Code", y="Life expectancy (years)", histfunc='avg')
fig3.update_layout(bargap=0.2)

fig4 = px.histogram(df, x="Code", y="Life expectancy (years)", histfunc='min')
fig4.update_layout(bargap=0.2)

fig5 = px.histogram(df, x="Code", y="Life expectancy (years)", histfunc='max')
fig5.update_layout(bargap=0.2)

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Expectativa de vida, analises (ocorrencia,soma,média,minimo,maximo)'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    dcc.Graph(
        id='example-graph1',
        figure=fig2
    ),
    dcc.Graph(
        id='example-graph2',
        figure=fig3
    ),
    dcc.Graph(
        id='example-graph3',
        figure=fig4
    ),
    dcc.Graph(
        id='example-graph4',
        figure=fig5
    )

])

if __name__ == '__main__':
   app.run_server(debug=True, port=8056)

