from dash import Dash, html, dcc, Input, Output
import dash_daq as daq
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv(
    "C:/Users/usuario/Downloads/Emissions Data.csv"
)
df = df.query("Ano == 2008")
df1 = df.query("Emissao > 20.00")
df2 = df.query("Emissao > 10.00")

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


bar_slider = html.Div(
    [
        daq.GraduatedBar(
            id="bar",
            label="Filtro de emissoes:",
            value=5,
        ),
        html.Div(className='mb-5'),
        daq.Slider(
            id="slider",
            min=0,
            max=10,
            value=5,
            handleLabel={"showCurrentValue": True, "label": "VALUE"},
        ),
    ]
)

bar_slider2 = html.Div(
    [
        daq.GraduatedBar(
            id="bar2",
            label="Filtro de emissoes:",
            value=5,
        ),
        html.Div(className='mb-5'),
        daq.Slider(
            id="slider2",
            min=0,
            max=10,
            value=5,
            handleLabel={"showCurrentValue": True, "label": "VALUE"},
        ),
    ]
)

bar_slider3 = html.Div(
    [
        daq.GraduatedBar(
            id="bar3",
            label="Filtro de emissoes:",
            value=5,
        ),
        html.Div(className='mb-5'),
        daq.Slider(
            id="slider3",
            min=0,
            max=10,
            value=5,
            handleLabel={"showCurrentValue": True, "label": "VALUE"},
        ),
    ]
)

app.layout = dbc.Container(
    [
        html.H2("Filtrando grafico de emissao por escala de paises"),
        dbc.Row(
            [
                dbc.Col(bar_slider, md=4),
                dbc.Col(dcc.Graph(id="graph"), md=8),
            ],
            align="center",
        ),
        dbc.Row(
            [
                dbc.Col(bar_slider2, md=4),
                dbc.Col(dcc.Graph(id="graph1"), md=8),
            ],
            align="center",
        ),
        dbc.Row(
            [
                dbc.Col(bar_slider3, md=4),
                dbc.Col(dcc.Graph(id="graph2"), md=8),
            ],
            align="center",
        ),

    ],

)


@app.callback(
    Output("bar", "value"),
    Input("slider", "value"),
)
def update_output(value):
    return value


@app.callback(
    Output("graph", "figure"),
    Input("slider", "value"),

)
def update_graph(value):
    dff = df.loc[df["Emissao"] > value]
    fig = px.bar(
        dff,
        x="Paises",
        y="Emissao",
        title="Paises com emissao em 2011",
    )
    fig.update(layout=dict(title=dict(x=0.5)))
    return fig


@app.callback(
    Output("bar2", "value"),
    Input("slider2", "value"),
)
def update_output(value):
    return value
@app.callback(
    Output("graph1", "figure"),
    Input("slider2", "value"),

)
def update_graph2(value):
    dff = df1.loc[df1["Emissao"] > value]
    fig2 = px.bar(
        dff,
        x="Paises",
        y="Emissao",
        title="Paises com emissao acima de 20 milhoes",
    )
    fig2.update(layout=dict(title=dict(x=0.5)))
    return fig2



@app.callback(
    Output("bar3", "value"),
    Input("slider3", "value"),
)
def update_output(value):
    return value
@app.callback(
    Output("graph2", "figure"),
    Input("slider3", "value"),

)
def update_graph2(value):
    dff = df2.loc[df2["Emissao"] > value]
    fig3 = px.bar(
        dff,
        x="Ano",
        y="Continente",
        title="Continentes com emissao ate 25K de gases"
    )
    fig3.update(layout=dict(title=dict(x=0.5)))
    return fig3


if __name__ == "__main__":
    app.run_server(debug=True, port=8051)