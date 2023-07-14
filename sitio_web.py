import dash
from dash import dcc, html, callback, Output, Input, Dash, State
from flask import Flask, send_file
import os
#import dash_bootstrap_components as dbc
import base64
from joblib import dump, load

class Nodo:
    def __init__(
        self,
        arista: str="",
        etiqueta:str = "") ->None:
        self.arista=arista
        self.etiqueta=etiqueta
        self.hijos=[]

    def tiene_hijos(self):
        return len(self.hijos) != 0

    def __str__ (self)->str:
        return  str(self.arista) + " -> " + self.etiqueta
    
class Arbol:
    def __init__(self, raiz:Nodo)-> None:
        self.raiz = raiz

    def mostrar(self):
        self.__mostrar_arbol(self.raiz)

    def clasificar (self, ejemplo: dict):
        return self.__clasifica(ejemplo, self.raiz)

    def __clasifica(self,ejemplo:dict, nodo: Nodo) -> str:
        if not nodo.tiene_hijos():
            return nodo.etiqueta
        valor = ejemplo[nodo.etiqueta]
        for h in nodo.hijos:
            if h.arista == valor:
                #print(h)
                return self.__clasifica(ejemplo, h)

    def __mostrar_arbol(self, nodito:Nodo, nivel:int=0):
        #print("*"*50)
        print("\t"*nivel, end="")

        print(nodito)
        for hijo in nodito.hijos:
            #print("\t", end="")
            #print(hijo)
            self.__mostrar_arbol(hijo,nivel+1)




app = Dash(__name__)
server = app.server

modelo = load('modelo')

def image_to_base64(image_path):
    with open(image_path, 'rb') as f:
        image = f.read()
        encoded_image = base64.b64encode(image).decode('utf-8')
    return encoded_image

imagen_paths = {
    'btn-imagen1': 'imagen1.jpg',
    'btn-imagen2': 'imagen2.jpg',
    'btn-imagen3': 'imagen3.jpg',
    'btn-imagen4': 'imagen4.jpg',
    'btn-imagen5': 'imagen5.jpg',
    'btn-imagen6': 'imagen6.jpg',
    'btn-imagen7': 'imagen7.jpg',
    'btn-imagen8': 'imagen8.jpg',
    'btn-imagen9': 'imagen9.jpg',
    'btn-imagen10': 'imagen10.jpg',
    'btn-imagen11': 'imagen11.jpg',
    'btn-imagen12': 'imagen12.jpg',
    'btn-imagen13': 'imagen13.jpg',
    'btn-imagen14': 'imagen14.jpg',
    'btn-imagen15': 'imagen15.jpg',
    'btn-imagen16': 'imagen16.jpg',
    'btn-imagen17': 'imagen17.jpg',
    'btn-imagen18': 'imagen18.jpg',
    'btn-imagen19': 'imagen19.jpg',
    'btn-imagen20': 'imagen20.jpg',
    
}

@app.callback(
    Output('frame-imagen', 'src'),
    [Input(f'btn-imagen{i}', 'n_clicks') for i in range(1, 19)]
)
def mostrar_imagen(n_clicks, *botones):
    if n_clicks is None:
        return dash.no_update
    boton_id = dash.callback_context.triggered[0]['prop_id'].split('.')[0]
    imagen_path = imagen_paths.get(boton_id, '')
    encoded_image = image_to_base64(imagen_path)
    return f"data:image/jpg;base64,{encoded_image}"

@app.server.route('/download')
def serve_file():
    file_path = os.path.join(os.getcwd(), 'modelo')  
    return send_file(file_path, as_attachment=True)

with open('e13bbfba0edef0e5e9c55a787a6ade7e.jpg', 'rb') as f:
    image = f.read()
    encoded_image = base64.b64encode(image).decode('utf-8')

app.layout = html.Div(
    className='container',
    style={
        'background-image': 'url("data:image/jpg;base64,{}")'.format(encoded_image),
        'background-size': 'cover',
        'background-position': 'center',
        'background-repeat': 'no-repeat'
    },
    children=[
        html.Div(
            className='cover',
            children=[
                html.H1('Rodando sobre 2 ruedas', className='title'),
                html.H2('Bienvenido', className='subtitle')
            ]
        ),
        dcc.Tabs(
            id='tabs',
            value='cuestionario',
            children=[
                dcc.Tab(
                    label='Cuestionario',
                    value='cuestionario',
                    className='tab',
                    children=[
                        html.Div(
                            className='cuestionario-container',
                            children=[
                                html.H1('¿Le apetece comprar una nueva bicicleta? ¡Tome el siguiente test y averígüelo!',
                                        className='cuestionario-title'),
                                html.Div(id='preguntas-cuestionario'),
                                html.Div(
                                    className='btn-submit-container',
                                    children=[
                                        html.Button('Gracias por utilizar nuestro servicio', id='enviar-cuestionario', n_clicks=0, className='btn-submit')
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                dcc.Tab(
                    label='Gráficas',
                    value='graficas',
                    className='tab',
                    children=[
                        html.Div(
                            className='graficas-container',
                            children=[
                                html.H1('¡Exploremos la base de datos!', className='graficas-title'),
                                html.Div(
                                    className='botones-container',
                                    children=[
                                        html.Button('Income', id='btn-imagen1', n_clicks=0, className='btn-imagen'),
                                        html.Button('Children', id='btn-imagen2', n_clicks=0, className='btn-imagen'),
                                        html.Button('Education', id='btn-imagen3', n_clicks=0, className='btn-imagen'),
                                        html.Button('Home Owner', id='btn-imagen4', n_clicks=0, className='btn-imagen'),
                                        html.Button('Cars', id='btn-imagen5', n_clicks=0, className='btn-imagen'),
                                        html.Button('Commute Distance', id='btn-imagen6', n_clicks=0, className='btn-imagen'),
                                        html.Button('Age', id='btn-imagen7', n_clicks=0, className='btn-imagen'),
                                        html.Button('IsFemale', id='btn-imagen8', n_clicks=0, className='btn-imagen'),
                                        html.Button('IsMale', id='btn-imagen9', n_clicks=0, className='btn-imagen'),
                                        html.Button('IsMarried', id='btn-imagen10', n_clicks=0, className='btn-imagen'),
                                        html.Button('IsSingle', id='btn-imagen11', n_clicks=0, className='btn-imagen'),
                                        html.Button('Professional occupation', id='btn-imagen12', n_clicks=0, className='btn-imagen'),
                                        html.Button('Skilled Manual occupation', id='btn-imagen13', n_clicks=0, className='btn-imagen'),
                                        html.Button('Clerical occupation', id='btn-imagen14', n_clicks=0, className='btn-imagen'),
                                        html.Button('Management occupation', id='btn-imagen15', n_clicks=0, className='btn-imagen'),
                                        html.Button('Manual occupation', id='btn-imagen16', n_clicks=0, className='btn-imagen'),
                                        html.Button('FromNorthAmerica', id='btn-imagen17', n_clicks=0, className='btn-imagen'),
                                        html.Button('FromEurope', id='btn-imagen18', n_clicks=0, className='btn-imagen'),
                                        html.Button('FromPacific', id='btn-imagen19', n_clicks=0, className='btn-imagen'),
                                        html.Button('Purchased Bike', id='btn-imagen20', n_clicks=0, className='btn-imagen'),
                                        
                                    ]
                                ),
                                html.Div(
                                    id='imagen-container', 
                                    className='imagen-container',
                                    children=[
                                            html.Img(id='frame-imagen', style={'height':'40%', 'width':'40%'})
                                    ])
                                
                            ]
                        )
                    ]
                ),
                dcc.Tab(
                    label='Archivo',
                    value='nosotros',
                    className='tab',
                    children=[
                        html.Div(
                            className='nosotros-container',
                            children=[
                                html.H1('Archivo binario', className='nosotros-title'),
                                html.A('Descargar archivo binario', href='/download', className='download-link'),
                                
                            ]
                        )
                    ]
                )
            ],
            colors={
                'border': '#F0C808',
                'primary': '#F0C808',
                'background': '#F0C808'
            }
        ),
        html.Div(id='tab-content', className='tab-content')
    ]
)

diccionario = {}  

@app.callback(
    Output('preguntas-cuestionario', 'children'),
    [Input('tabs', 'value')]
)
def render_cuestionario(tab):
    if tab == 'cuestionario':
        preguntas = [
            {'pregunta': '¿Cuál es su ingreso?',
             'opciones': [
                 {'opcion': ' $10,000 - $40,000', 'valor': 'bajo'},
                 {'opcion': ' $40,001 - $80,000', 'valor': 'medio'},
                 {'opcion': ' $80,001 - $120,000', 'valor': 'alto'},
                 {'opcion': ' + $120,000', 'valor': 'muy_alto'}
             ]},
            {'pregunta': '¿Cuántos hijos tiene?',
             'opciones': [
                 {'opcion': ' 0', 'valor': '0'},
                 {'opcion': ' 1', 'valor': '1'},
                 {'opcion': ' 2', 'valor': '2'},
                 {'opcion': ' 3', 'valor': '3'},
                 {'opcion': ' 4', 'valor': '4'},
                 {'opcion': ' 5', 'valor': '5'}
            ]},
            {'pregunta': '¿Cuál es su grado de educación?',
             'opciones': [
                 {'opcion': ' Parcialmente Preparatoria', 'valor': 'Partial High School'},
                 {'opcion': ' Preparatoria', 'valor': 'High School'},
                 {'opcion': ' Parcialmente Colegio', 'valor': 'Partial College'},
                 {'opcion': ' Licenciatura', 'valor': 'Bachelors'},
                 {'opcion': ' Postgrado', 'valor': 'Graduate Degree'}
             ]},
            {'pregunta': '¿Es dueño de una casa?',
             'opciones': [
                 {'opcion': ' Si', 'valor': 'Yes'},
                 {'opcion': ' No', 'valor': 'No'}
             ]},
             {'pregunta': '¿Cuántos carros tiene?',
             'opciones': [
                 {'opcion': ' 0', 'valor': '0'},
                 {'opcion': ' 1', 'valor': '1'},
                 {'opcion': ' 2', 'valor': '2'},
                 {'opcion': ' 3', 'valor': '3'},
                 {'opcion': ' 4', 'valor': '4'}
            ]},
            {'pregunta': '¿Cuál es su distancia recorrida?',
             'opciones': [
                 {'opcion': ' 0 - 1 millas', 'valor': '0-1 Miles'},
                 {'opcion': ' 1 - 2 millas', 'valor': '1-2 Miles'},
                 {'opcion': ' 2 - 5 millas', 'valor': '2-5 Miles'},
                 {'opcion': ' 5 - 10 millas', 'valor': '5-10 Miles'},
                 {'opcion': ' + 10 millas', 'valor': '10+ Miles'}

             ]},
            {'pregunta': '¿Cuál es su edad?',
             'opciones': [
                 {'opcion': ' 20 - 40 años', 'valor': '20-40'},
                 {'opcion': ' 41 - 60 años', 'valor': '41-60'},
                 {'opcion': ' 61 - 80 años', 'valor': '61-80'},
                 {'opcion': ' 81 - 100 años', 'valor': '81-100'},
                 {'opcion': ' + 100 años', 'valor': '+100'}
             ]},
            {'pregunta': '¿Es mujer?',
             'opciones': [
                 {'opcion': ' Si', 'valor': 'Yes'},
                 {'opcion': ' No', 'valor': 'No'}
             ]},
            {'pregunta': '¿Es hombre?',
             'opciones': [
                 {'opcion': ' Si', 'valor': 'Yes'},
                 {'opcion': ' No', 'valor': 'No'}
            ]},
            {'pregunta': '¿Es casada o casado?',
             'opciones': [
                 {'opcion': ' Si', 'valor': 'Yes'},
                 {'opcion': ' No', 'valor': 'No'}
             ]},
            {'pregunta': '¿Es soltera o soltero?',
             'opciones': [
                 {'opcion': ' Si', 'valor': 'Yes'},
                 {'opcion': ' No', 'valor': 'No'}
            ]},
            {'pregunta': '¿Ejerce profesionalmente?',
             'opciones': [
                 {'opcion': ' Si', 'valor': 'Yes'},
                 {'opcion': ' No', 'valor': 'No'}
             ]},
            {'pregunta': '¿Ejerce ocupación manual calificada?',
             'opciones': [
                 {'opcion': ' Si', 'valor': 'Yes'},
                 {'opcion': ' No', 'valor': 'No'}
            ]},
            {'pregunta': '¿Ejerce ocuapción clerical?',
             'opciones': [
                 {'opcion': ' Si', 'valor': 'Yes'},
                 {'opcion': ' No', 'valor': 'No'}
             ]},
            {'pregunta': '¿Ejerce ocupación gerencial o administrativa?',
             'opciones': [
                 {'opcion': ' Si', 'valor': 'Yes'},
                 {'opcion': ' No', 'valor': 'No'}
            ]},
            {'pregunta': '¿Ejerce ocupación manual?',
             'opciones': [
                 {'opcion': ' Si', 'valor': 'Yes'},
                 {'opcion': ' No', 'valor': 'No'}
             ]},
            {'pregunta': '¿Es de Norte América?',
             'opciones': [
                 {'opcion': ' Si', 'valor': 'Yes'},
                 {'opcion': ' No', 'valor': 'No'}
             ]},
            {'pregunta': '¿Es de Europa?',
             'opciones': [
                 {'opcion': ' Si', 'valor': 'Yes'},
                 {'opcion': ' No', 'valor': 'No'}
             ]},
            {'pregunta': '¿Es del Pacífico?',
             'opciones': [
                 {'opcion': ' Si', 'valor': 'Yes'},
                 {'opcion': ' No', 'valor': 'No'}
            ]},
            
            
        ]
        
        return html.Div([
            html.H2('Cuestionario', className='cuestionario-subtitle'),
            html.Div(id='respuestas-cuestionario'),
            html.Button('Enviar', id='enviar-cuestionario', n_clicks=0, className='btn-submit')
        ] + [
            html.Div([
                html.H3(pregunta['pregunta']),
                dcc.RadioItems(
                    id={'type': 'radio-opcion', 'index': index},
                    options=[{'label': opcion['opcion'], 'value': opcion['valor']} for opcion in pregunta['opciones']]
                )
            ]) for index, pregunta in enumerate(preguntas)
        ])
    else:
        return html.Div()

@app.callback(
    [Output('respuestas-cuestionario', 'children'),
     Output('tab-content', 'children')],
    [Input({'type': 'radio-opcion', 'index': dash.dependencies.ALL}, 'value'),
     Input('enviar-cuestionario', 'n_clicks')],
    [State('tabs', 'value')]
)
def update_respuestas_cuestionario(values, n_clicks, tab):
    global diccionario  

    preguntas = [
        'Income',
        'Children',
        'Education',
        'Home Owner',
        'Cars',
        'Commute Distance',
        'Age',
        'IsFemale',
        'IsMale',
        'IsMarried',
        'IsSingle',
        'Professional occupation',
        'Skilled Manual occupation',
        'Clerical occupation',
        'Management occupation',
        'Manual occupation',
        'FromNorthAmerica',
        'FromEurope',
        'FromPacific'
    ]
    
    respuestas = {
        preguntas[i]: int(value) if value is not None and preguntas[i] in ['Children', 'Cars'] else value
        for i, value in enumerate(values)
    }
    diccionario = respuestas  

    if tab == 'cuestionario':
        if n_clicks > 0:
            
            resultado = modelo.clasificar(diccionario)

            
            mensaje = None
            if resultado == 'Yes':
                mensaje = "¡Es momento de comprar una bicicleta! ¡A entrenar!"
            elif resultado == 'No':
                mensaje = "¡Mejor invertamos el dinero en algo diferente!"
            else:
                mensaje = "¡Uy! Parece que es necesario considerar otros factores para tomar esa decisión."

            return (
                None,  
                html.H3(f"Resultado: {mensaje}")
            )
        else:
            return None, None  
    else:
        return None, html.H3("")  



if __name__ == '__main__':
    app.run_server(debug=False)

