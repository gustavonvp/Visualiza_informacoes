# This is a sample Python script.
import csv
import pathlib

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import plotly.express as px
from collections import OrderedDict
import sklearn.svm
from dash import Dash, html, dash_table, dcc, Input, Output
import dash_mantine_components as dmc
import dash_daq as daq

import json
import sys

from hpsklearn import HyperoptEstimator, svc
from sklearn import svm
# Defining the columns to read
usecols = ["iso_code", "country", "year", "co2", "co2_per_capita", "trade_co2", "cement_co2", "cement_co2_per_capita",
           "coal_co2", "coal_co2_per_capita", "flaring_co2", "flaring_co2_per_capita", "gas_co2", "gas_co2_per_capita",
           "oil_co2", "oil_co2_per_capita", "other_industry_co2", "other_co2_per_capita", "co2_growth_prct",
           "co2_growth_abs", "co2_per_gdp", "co2_per_unit_energy", "consumption_co2", "consumption_co2_per_capita",
           "consumption_co2_per_gdp", "cumulative_co2", "cumulative_cement_co2", "cumulative_coal_co2",
           "cumulative_flaring_co2", "cumulative_gas_co2", "cumulative_oil_co2", "cumulative_other_co2",
           "trade_co2_share", "share_global_co2", "share_global_cement_co2", "share_global_coal_co2",
           "share_global_flaring_co2", "share_global_gas_co2", "share_global_oil_co2", "share_global_other_co2",
           "share_global_cumulative_co2", "share_global_cumulative_cement_co2", "share_global_cumulative_coal_co2",
           "share_global_cumulative_flaring_co2", "share_global_cumulative_gas_co2", "share_global_cumulative_oil_co2",
           "share_global_cumulative_other_co2", "total_ghg", "ghg_per_capita", "total_ghg_excluding_lucf",
           "ghg_excluding_lucf_per_capita", "methane", "methane_per_capita", "nitrous_oxide",
           "nitrous_oxide_per_capita", "population", "gdp", "primary_energy_consumption", "energy_per_capita",
           "energy_per_gdp"

           ]



# Load Data
# ...
data1 = (

    pd.read_csv("C:/Users/usuario/Downloads/owid-co2-data.csv", usecols=usecols)

    #    .query("'year'")

    #   .assign(population=lambda x: 'gpd' / 'population' )
    #  .sort_values(by="year")

)

data1.head()

#data = OrderedDict(
    #                [   ("country",["year", "co2"]),
   #                     ("co2_per_capita",["trade_co2", "cement_co2"]),
  #                  ]
 #                  )
#df = pd.DataFrame(data)
# <<show score here>>



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(external_stylesheets=external_stylesheets)

#app1 = Dash(__name__)

#app1.layout = dash_table.DataTable(
 #   data=df.to_dict('records'),
  #  columns=[{'id': c, 'country': c} for c in df.columns]
#)

df = px.data.gapminder()
df = df.loc[df["pop"] > 1e8]

app.layout = [

    # App layout
    html.H2("Turning a Graph On and Off with BooleanSwitch"),
    html.P("graph off | graph on:", style={"textAlign": "center"}),
    daq.BooleanSwitch(id="pb", on=True),

    html.Div(id="pb-result", children = 'Aplicativo sobre CO2 em rank Mundial', style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),
    html.P("Selecione uma categoria de analise de co2:"),
    html.Div(className='row', children=[
        dcc.RadioItems(
            id='graph1',
            options=["iso_code", "country", "year", "co2", "co2_per_capita", "trade_co2", "cement_co2",
                     "cement_co2_per_capita",
                     "coal_co2", "coal_co2_per_capita", "flaring_co2", "flaring_co2_per_capita", "gas_co2",
                     "gas_co2_per_capita",
                     "oil_co2", "oil_co2_per_capita", "other_industry_co2", "other_co2_per_capita", "co2_growth_prct",
                     "co2_growth_abs", "co2_per_gdp", "co2_per_unit_energy", "consumption_co2",
                     "consumption_co2_per_capita",
                     "consumption_co2_per_gdp", "cumulative_co2", "cumulative_cement_co2", "cumulative_coal_co2",
                     "cumulative_flaring_co2", "cumulative_gas_co2", "cumulative_oil_co2", "cumulative_other_co2",
                     "trade_co2_share", "share_global_co2", "share_global_cement_co2", "share_global_coal_co2",
                     "share_global_flaring_co2", "share_global_gas_co2", "share_global_oil_co2",
                     "share_global_other_co2",
                     "share_global_cumulative_co2", "share_global_cumulative_cement_co2",
                     "share_global_cumulative_coal_co2",
                     "share_global_cumulative_flaring_co2", "share_global_cumulative_gas_co2",
                     "share_global_cumulative_oil_co2",
                     "share_global_cumulative_other_co2", "total_ghg", "ghg_per_capita", "total_ghg_excluding_lucf",
                     "ghg_excluding_lucf_per_capita", "methane", "methane_per_capita", "nitrous_oxide",
                     "nitrous_oxide_per_capita", "population", "gdp", "primary_energy_consumption", "energy_per_capita",
                     "energy_per_gdp"],
            value="country",
            inline=True
        ),

    ]),



    dash_table.DataTable(data=data1.to_dict('records'), page_size=10,style_table={'overflowX': 'auto'}),
    dcc.Graph(id="graph", figure={})

]

@app.callback(
    Output(component_id='graph', component_property='figure'),
    Input(component_id='graph1', component_property='value'))
def update_graph(col_chosen):
    fig = px.histogram(data1, x='country', y=col_chosen, histfunc='avg')
 #   geojson = px.data.election_geojson()
 #   fig = px.choropleth(
  #      iso_code, geojson=geojson, color='iso_code',
   #     locations="iso_code", featureidkey="properties.iso_code",
    #    projection="cylindrical equal area", range_color=[0, 6500])
    #fig.update_geos(fitbounds="locations", visible=False)
    #fig.update_layout(margin={"r":100,"t":100,"l":50,"b":50})
    return fig
# Add controls to build the interaction

@app.callback(
    Output("pb-result", "children"),
    Input("pb", "on"),
)
def update_output(on):
    if on:
        fig = px.line(
            df,
            x="year",
            y="lifeExp",
            color="country",
            markers=True,
            title="Life Expectancy for Countries with High Population",
        )
        fig.update(layout=dict(title=dict(x=0.5)))
        return dcc.Graph(figure=fig)
    else:
        fig = px.scatter()
        return dcc.Graph(figure=fig)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

if __name__ == "__main__":
    # if sklearn.svm.NuSVC:
    # stim = HyperoptEstimator(classifier=svc("mySVC"))
    # el      ese:
    # estim = svm.SVC()
    # estim.fit(X_train, y_train)

    # print(estim.score(X_test, y_test))

    app.run_server(debug=True)