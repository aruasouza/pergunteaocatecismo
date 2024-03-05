from dash import Dash, html, dcc, callback, Output, Input, State
from search import ask

app = Dash(__name__,title = 'Pergunte ao Catecismo')

app.layout = html.Div([
    html.H1('Pergunte ao Catecismo',className = 'title'),
    html.Div([
        dcc.Input(placeholder = 'Faça uma pergunta.',id = 'pergunta',autoFocus = True),
        html.Button(html.Img(src = 'assets/send.png',width = '50px',height = '50px'),id = 'send')
    ],className = 'input'),
    html.Div([],id = 'respostas')
],className = 'main-div')

@callback(
    Output('respostas','children'),
    Input('send','n_clicks'),
    State('pergunta','value')
)
def update_respostas(n,pergunta):
    respostas = ask(pergunta)
    return [html.Div(resp,className = 'resp') for resp in respostas]