from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px


from create_dataframe import DataFrame
from utilities import casos_novos_regiao


brasil, regiao = DataFrame().format()

casos_regiao = casos_novos_regiao(regiao, 'casosNovos')
obitos_regiao = casos_novos_regiao(regiao, 'obitosNovos')

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Painel Geral", href="#", style={'color': 'black'})),
    ],
    brand="Painel Coronavírus",
    brand_style={'color': 'black'},
    brand_href="#",
    color="light",
    dark=True,
)

card_recuperado = [
    dbc.CardBody(
        [
            html.H4("Casos Recuperados", className="card-title"),
            html.H1(
                format(
                    int(
                        brasil.set_index(keys='data').loc[
                            brasil.set_index(keys='data').last_valid_index().strftime('%Y-%m-%d'), 'casosAcumulado'
                        ]
                    ), ',d'
                ).replace(',', '.'),
                className="card-text",
            ),
            html.H5("Em acompanhamento", className="card-title"),
            html.H2(
                format(
                    int(
                        brasil.set_index(keys='data').loc[
                            brasil.set_index(keys='data').last_valid_index().strftime('%Y-%m-%d'),
                            'emAcompanhamentoNovos'
                        ]
                    ), ',d'
                ).replace(',', '.'),
                className="card-text",
            ),
        ]
    ),
]

card_casos = [
    dbc.CardHeader("Casos Confirmados"),
    dbc.CardBody(
        [
            html.H6("Novos", className="card-title"),
            html.H2(
                format(
                    int(
                        brasil.set_index(keys='data').loc[
                            brasil.set_index(keys='data').last_valid_index().strftime('%Y-%m-%d'), 'casosNovos'
                        ]
                    ), ',d'
                ).replace(',', '.'),
                className="card-text",
            ),
            html.H6("Acumulados", className="card-title"),
            html.H2(
                format(
                    int(
                        brasil.set_index(keys='data').loc[
                            brasil.set_index(keys='data').last_valid_index().strftime('%Y-%m-%d'),
                            'casosAcumulado'
                        ]
                    ), ',d'
                ).replace(',', '.'),
                className="card-text",
            ),
        ]
    ),
]

card_obitos = [
    dbc.CardHeader("Óbitos Confirmados"),
    dbc.CardBody(
        [
            html.H6("Novos", className="card-title"),
            html.H2(
                format(
                    int(
                        brasil.set_index(keys='data').loc[
                            brasil.set_index(keys='data').last_valid_index().strftime('%Y-%m-%d'), 'obitosNovos'
                        ]
                    ), ',d'
                ).replace(',', '.'),
                className="card-text",
            ),
            html.H6("Acumulados", className="card-title"),
            html.H2(
                format(
                    int(
                        brasil.set_index(keys='data').loc[
                            brasil.set_index(keys='data').last_valid_index().strftime('%Y-%m-%d'), 'obitosAcumulado'
                        ]
                    ), ',d'
                ).replace(',', '.'),
                className="card-text",
            ),
        ]
    ),
]


cards = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(card_recuperado, color="success", inverse=True)),
                dbc.Col(dbc.Card(card_casos, color="warning", outline=True)),
                dbc.Col(dbc.Card(card_obitos, color="danger", outline=True))
            ],
            className="mb-4",
        )
    ]
)

accordion = html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    dbc.Table.from_dataframe(
                        (
                            regiao[regiao.regiao == 'Norte']
                            .drop(labels=['casosAcumulado', 'obitosAcumulado', 'data'], axis=1)
                            .groupby(by=['regiao', 'estado']).sum().reset_index()
                            .rename(mapper={'casosNovos': 'casos', 'obitosNovos': 'obitos'}, axis=1)
                            .applymap(lambda x: "{:,}".format(int(x)).replace(',', '.') if isinstance(x, int) else x)
                        ),
                        striped=True, bordered=True, hover=True
                    )
                ],
                title="Norte",
            ),
            dbc.AccordionItem(
                [
                    dbc.Table.from_dataframe(
                        (
                            regiao[regiao.regiao == 'Nordeste']
                            .drop(labels=['casosAcumulado', 'obitosAcumulado', 'data'], axis=1)
                            .groupby(by=['regiao', 'estado']).sum().reset_index()
                            .rename(mapper={'casosNovos': 'casos', 'obitosNovos': 'obitos'}, axis=1)
                            .applymap(lambda x: "{:,}".format(int(x)).replace(',', '.') if isinstance(x, int) else x)
                        ),
                        striped=True, bordered=True, hover=True
                    )
                ],
                title="Nordeste",
            ),
            dbc.AccordionItem(
                [
                    dbc.Table.from_dataframe(
                        (
                            regiao[regiao.regiao == 'Centro-Oeste']
                            .drop(labels=['casosAcumulado', 'obitosAcumulado', 'data'], axis=1)
                            .groupby(by=['regiao', 'estado']).sum().reset_index()
                            .rename(mapper={'casosNovos': 'casos', 'obitosNovos': 'obitos'}, axis=1)
                            .applymap(lambda x: "{:,}".format(int(x)).replace(',', '.') if isinstance(x, int) else x)
                        ),
                        striped=True, bordered=True, hover=True
                    )
                ],
                title="Centro-Oeste",
            ),
            dbc.AccordionItem(
                [
                    dbc.Table.from_dataframe(
                        (
                            regiao[regiao.regiao == 'Sul']
                            .drop(labels=['casosAcumulado', 'obitosAcumulado', 'data'], axis=1)
                            .groupby(by=['regiao', 'estado']).sum().reset_index()
                            .rename(mapper={'casosNovos': 'casos', 'obitosNovos': 'obitos'}, axis=1)
                            .applymap(lambda x: "{:,}".format(int(x)).replace(',', '.') if isinstance(x, int) else x)
                        ),
                        striped=True, bordered=True, hover=True
                    )
                ],
                title="Sul",
            ),
            dbc.AccordionItem(
                [
                    dbc.Table.from_dataframe(
                        (
                            regiao[regiao.regiao == 'Sudeste']
                            .drop(labels=['casosAcumulado', 'obitosAcumulado', 'data'], axis=1)
                            .groupby(by=['regiao', 'estado']).sum().reset_index()
                            .rename(mapper={'casosNovos': 'casos', 'obitosNovos': 'obitos'}, axis=1)
                            .applymap(lambda x: "{:,}".format(int(x)).replace(',', '.') if isinstance(x, int) else x)
                        ),
                        striped=True, bordered=True, hover=True
                    )
                ],
                title="Sudeste",
            ),
        ], start_collapsed=True,
    )
)

select_casos = dbc.Select(
    id="select_casos",
    options=[
        {'label': 'Norte', 'value': 'Norte'},
        {'label': 'Nordeste', 'value': 'Nordeste'},
        {'label': 'Sul', 'value': 'Sul'},
        {'label': 'Sudeste', 'values': 'Sudeste'},
        {'label': 'Centro-Oeste', 'value': 'Centro-Oeste'}
    ], value='Sul'
)

select_obitos = dbc.Select(
    id="select_obitos",
    options=[
        {'label': 'Norte', 'value': 'Norte'},
        {'label': 'Nordeste', 'value': 'Nordeste'},
        {'label': 'Sul', 'value': 'Sul'},
        {'label': 'Sudeste', 'values': 'Sudeste'},
        {'label': 'Centro-Oeste', 'value': 'Centro-Oeste'}
    ], value='Sul'
)

fig_brasil_casos_novos = px.line(
    brasil.set_index(keys='data').loc[:, ['casosNovos']].resample('M').sum().reset_index(),
    x='data', y='casosNovos', title='Casos Novos'
)

fig_brasil_casos_acumulados = px.line(
    brasil, x='data', y='casosAcumulado', title='Casos Acumulados'
)

fig_brasil_obitos_novos = px.line(
    brasil.set_index(keys='data').loc[:, ['obitosNovos']].resample('M').sum().reset_index(),
    x='data', y='obitosNovos', title='Óbitos Novos'
)

fig_brasil_obitos_acumulados = px.line(
    brasil, x='data', y='obitosAcumulado', title='Óbitos Acumulados'
)

app.layout = dbc.Container(
    [
        navbar, dbc.Label(f"Atualizado em: {max(brasil.data).strftime('%d-%m-%Y')}"), html.Hr(), cards, html.Hr(),
        html.P('Síntense de casos e óbitos'), accordion, html.Hr(), html.P('Estatísticas do Brasil'), dbc.Row(
            [
                dbc.Col(dcc.Graph(id='grafico_casos_novos', figure=fig_brasil_casos_novos), md=6),
                dbc.Col(dcc.Graph(id='grafico_casos_acumulados', figure=fig_brasil_casos_acumulados), md=6)
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='grafico_obitos_novos', figure=fig_brasil_obitos_novos), md=6),
                dbc.Col(dcc.Graph(id='grafico_obitos_acumulados', figure=fig_brasil_obitos_acumulados), md=6)
            ]
        ),
        html.Hr(), dbc.Row(
            [
                dbc.Col(select_casos),
                dbc.Col(select_obitos)

            ]
        ), dbc.Row(
            [
                dbc.Col(dcc.Graph(id='grafico_casos_regiao')),
                dbc.Col(dcc.Graph(id='grafico_obitos_regiao'))
            ]
        )
    ], fluid=True
)


@app.callback(
    Output("grafico_casos_regiao", 'figure'),
    Input('select_casos', 'value')
)
def update_fig(input_value):
    fig = px.line(
        casos_regiao[casos_regiao.regiao == input_value], x='data', y='casosNovos', color='estado',
        title='Casos Novos por Região'
    )
    return fig


@app.callback(
    Output("grafico_obitos_regiao", 'figure'),
    Input('select_obitos', 'value')
)
def update_fig(input_value):
    fig = px.line(
        obitos_regiao[obitos_regiao.regiao == input_value], x='data', y='obitosNovos', color='estado',
        title='Obitos Novos por Região'
    )
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
