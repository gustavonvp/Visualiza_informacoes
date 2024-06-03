# This is a sample Python script.
import csv
import pathlib

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import plotly.express as px
from dash import Dash, html, dash_table, dcc, Input, Output
import json
import sys

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



data1 = (

    pd.read_csv("C:/Users/usuario/Downloads/owid-co2-data.csv", usecols=usecols)

    #    .query("'year'")

    #   .assign(population=lambda x: 'gpd' / 'population' )
    #  .sort_values(by="year")

)
data1.head()




app = Dash()


@app.callback(
    Output("graph1", "figure"),
    Input("country", "value"))
def display_choropleth(iso_code):
    df = data1 # replace with your own data source
    geojson = px.data.election_geojson()
    fig = px.choropleth(
        df, geojson=geojson, color='iso_code',
        locations="iso_code", featureidkey="properties.iso_code",
        projection="cylindrical equal area", range_color=[0, 6500])
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":100,"t":100,"l":50,"b":50})
    return fig


app.layout = [

    # App layout

    html.Div(children = 'Aplicativo sobre CO2 em rank Mundial'),
    html.P("Selecione um pais:"),
    dcc.RadioItems(
        id='country',
        options=["Abecásia", "Afeganistão", "África do Sul", "Albânia", "Alemanha", "Andorra", "Angola", "Antígua e Barbuda", "Arábia Saudita", "Argélia", "Argentina", "Armênia", "Austrália", "Áustria", "Azerbaijão", "Bahamas", "Bahrein", "Bangladesh", "Barbados", "Bélgica", "Belize", "Benim", "Bielorrússia", "Bolívia", "Bósnia e Herzegovina", "Botswana", "Brasil", "Brunei", "Bulgária", "Burkina Faso", "Burundi", "Butão", "Cabo Verde", "Camarões", "Camboja", "Canadá", "Catar", "Cazaquistão", "Chade", "Chile", "China", "Chipre", "Cingapura", "Colômbia", "Comores", "Congo", "Coreia do Norte", "Coreia do Sul", "Costa do Marfim", "Costa Rica", "Croácia", "Cuba", "Dinamarca", "Djibouti", "Dominica", "Egito", "El Salvador", "Emirados Árabes Unidos", "Equador", "Eritreia", "Escócia", "Eslováquia", "Eslovênia", "Espanha", "Estados Federados da Micronésia", "Estados Unidos da América", "Estônia", "Eswatini", "Etiópia", "Fiji", "Filipinas", "Finlândia", "França", "Gabão", "Gâmbia", "Gana", "Geórgia", "Granada", "Grécia", "Guatemala", "Guiana", "Guiné", "Guiné-Bissau", "Guiné Equatorial", "Haiti", "Holanda", "Honduras", "Hungria", "Iêmen", "Índia", "Indonésia", "Inglaterra", "Irã", "Iraque", "Irlanda do Norte", "Irlanda", "Islândia", "Israel", "Itália", "Jamaica", "Japão", "Jordânia", "Kiribati", "Kosovo", "Kuwait", "Laos", "Lesoto", "Letônia", "Líbano", "Libéria", "Líbia", "Liechtenstein", "Lituânia", "Luxemburgo", "Macedônia do Norte", "Madagascar", "Malásia", "Malawi", "Maldivas", "Mali", "Malta", "Marrocos", "Marshall", "Maurícia", "Mauritânia", "México", "Mianmar", "Micronésia", "Moçambique", "Moldávia", "Mônaco", "Mongólia", "Montenegro", "Namíbia", "Nauru", "Nepal", "Nicarágua", "Níger", "Nigéria", "Noruega", "Nova Zelândia", "Omã", "Ossétia do Sul", "País de Gales", "Países Baixos", "Palau", "Palestina", "Panamá", "Papua-Nova Guiné", "Paquistão", "Paraguai", "Peru", "Polônia", "Portugal", "Qatar", "Quênia", "Quirguistão", "Quiribati", "Reino Unido", "República Árabe Saaraui Democrática", "República Centro-Africana", "República Democrática do Congo", "República do Congo", "República Dominicana", "República Tcheca", "República Turca de Chipre do Norte", "Romênia", "Ruanda", "Rússia", "Salomão", "Samoa", "San Marino", "Santa Lúcia", "São Cristóvão e Névis", "São Tomé e Príncipe", "São Vicente e Granadinas", "Senegal", "Serra Leoa", "Sérvia", "Seychelles", "Singapura", "Síria", "Somália", "Sri Lanka", "Suazilândia", "Sudão do Sul", "Sudão", "Suécia", "Suíça", "Suriname", "Tailândia", "Taiwan", "Tajiquistão", "Tanzânia", "Tchéquia", "Timor-Leste", "Togo", "Tonga", "Trinidad e Tobago", "Tunísia", "Turcomenistão", "Turquia", "Tuvalu", "Ucrânia", "Uganda", "Uruguai", "Uzbequistão", "Vanuatu", "Vaticano", "Venezuela", "Vietnã", "Zâmbia", "Zimbábue" ],
        value="Brasil",
        inline=True
    ),
    dcc.Graph(id="graph1"),
    dash_table.DataTable(data=data1.to_dict('records'), page_size=10),
    dcc.Graph(id="graph", figure=px.histogram(data1, x='country', y='co2', histfunc='avg'))
]




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

if __name__ == "__main__":
    app.run_server(debug=True)
