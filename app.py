# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import openpyxl

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("Vendas.xlsx")

#CRIANDO OS GRÁFICOS
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
opcoes = list(df['ID Loja'].unique())
opcoes.append('Todas as Lojas')

app.layout = html.Div(children=[
    html.H1(children='Faturamento Loja'),
    html.H2(children="Gráfico com o Faturamento de Todos os Produtos, separados por loja"),
    html.Div(children='''
        Obs: Esse gráfico mostra a quantidade de produtos vendidos, não o faturamento.
    '''),
    dcc.Dropdown(opcoes, value='Todas as Lojas', id='lista_lojas'),

    dcc.Graph(
        id='grafico_quantidade_vendas',
        figure=fig
    )
])


@app.callback(
    Output('grafico_quantidade_vendas', 'figure'),#id para identificação, #parametro
    Input('lista_lojas', 'value')
)
def update_output(value):#Recebe o parametro "VALUE" como parametro
    if value == 'Todas as Lojas':
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df['ID Loja']==value,:]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig #RECEBE DO INPUT E RETORNA O VALOR DO OUTPUT


#SERVE PARA SUBIR NUM SITE
if __name__ == '__main__':
    app.run_server(debug=True)
