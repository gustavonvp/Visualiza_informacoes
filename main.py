import pandas as pd
import plotly.express as px

from dash import Dash, html, dash_table, dcc, Input, Output
import dash_daq as daq

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

)

data1.head()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(external_stylesheets=external_stylesheets)

app.layout = [

    # App layout
    html.Div(id="pb-result", children='Aplicativo sobre CO2 em rank Mundial',
             style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),
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

    #Print graph datable and figure dataplot

    dash_table.DataTable(data=data1.to_dict('records'), page_size=10, style_table={'overflowX': 'auto'}),
    dcc.Graph(id="graph", figure={})

]


@app.callback(
    Output(component_id='graph', component_property='figure'),
    Input(component_id='graph1', component_property='value'))
def update_graph(col_chosen):
    fig = px.histogram(data1, x='country', y=col_chosen, histfunc='avg', barmode="group")
    return fig


# Add controls to build the interaction


if __name__ == "__main__":
    app.run_server(debug=True, port=8052)
