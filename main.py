# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import plotly.express as px
from dash import Dash, html, dash_table, dcc

# Defining the columns to read
usecols = ["year", "iso_code", "population", "gdp", "cement_co2", "cement_co2_per_capita", "co2", "co2_growth_abs", "co2_growth_prct", "co2_including_luc",
           "co2_including_luc_growth_abs", "co2_including_luc_growth_prct", "co2_including_luc_per_capita", "co2_including_luc_per_gdp", "co2_including_luc_per_unit_energy", "co2_per_capita", "co2_per_gdp",
           "co2_per_unit_energy", "coal_co2", "coal_co2_per_capita", "consumption_co2", "consumption_co2_per_capita", "consumption_co2_per_gdp", "cumulative_cement_co2", "cumulative_co2", "cumulative_co2_including_luc",
           "cumulative_coal_co2", "cumulative_flaring_co2", "cumulative_gas_co2", "cumulative_luc_co2", "cumulative_oil_co2","cumulative_other_co2", "energy_per_capita", "energy_per_gdp", "flaring_co2", "flaring_co2_per_capita",
           "gas_co2", "gas_co2_per_capita", "ghg_excluding_lucf_per_capita", "ghg_per_capita", "land_use_change_co2", "land_use_change_co2_per_capita", "methane", "methane_per_capita", "nitrous_oxide", "nitrous_oxide_per_capita", "oil_co2", "oil_co2_per_capita",
           "other_co2_per_capita", "other_industry_co2", "primary_energy_consumption", "share_global_cement_co2", "share_global_co2_including_luc", "share_global_coal_co2", "share_global_cumulative_cement_co2", "share_global_cumulative_co2", "share_global_cumulative_co2_including_luc",
           "share_global_cumulative_coal_co2", "share_global_cumulative_flaring_co2", "share_global_cumulative_gas_co2", "share_global_cumulative_luc_co2", "share_global_cumulative_oil_co2", "share_global_cumulative_other_co2", "share_global_flaring_co2", "share_global_gas_co2", "share_global_luc_co2",
           "share_global_oil_co2", "share_global_other_co2", "share_of_temperature_change_from_ghg", "temperature_change_from_ch4", "temperature_change_from_co2", "temperature_change_from_ghg", "temperature_change_from_n2o", "total_ghg", "total_ghg_excluding_lucf",
           "trade_co2", "trade_co2_share"

           ]

data = (

    pd.read_csv("/home/koen/Documents/visualizing_global_co2_data.csv", usecols=usecols)


#    .query("'year'")

 #   .assign(population=lambda x: 'gpd' / 'population' )
  #  .sort_values(by="year")

)
data.head()

app = Dash()

app.layout = [

    # App layout

    html.Div(children='My First App with Data'),
    dash_table.DataTable(data=data.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(data, x='year', y='cement_co2', histfunc='avg'))
]


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

if __name__ == "__main__":
    app.run_server(debug=True)