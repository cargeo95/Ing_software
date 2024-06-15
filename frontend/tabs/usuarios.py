# Importamos las librerías necesarias de Dash y otros módulos
from dash import html, dcc
import dash_bootstrap_components as dbc

# Definimos el diseño (layout) para la pestaña de registrar usuarios
usuarios = dbc.Container([
    html.Br(), html.Br(),  # Añadimos saltos de línea para espaciar los elementos
    html.H3("Registrar usuarios"),  # Encabezado para la sección de registro de usuarios
    html.Hr(),  # Línea horizontal para separar el encabezado del contenido

    # Definimos una fila utilizando componentes de Bootstrap
    dbc.Row([
        # Primera columna que contiene el formulario de registro
        dbc.Col([
            html.Div([
                # Contenedor principal para el formulario
                html.Div([
                    # Div para el campo de entrada del nombre
                    html.Div([
                        html.Label("Nombre:", className='col-sm-3 col-form-label'),  # Etiqueta del campo
                        html.Div(dcc.Input(id='nombre', placeholder='Ingrese nombre del usuario', type='text', className='form-control'), className='col-sm-9'),
                        html.Br(), html.Br(), html.Br()  # Añadimos saltos de línea para espaciar
                    ], className='form-group row'),

                    # Div para el campo de entrada de la identificación
                    html.Div([
                        html.Label("Identificación:", className='col-sm-3 col-form-label'),  # Etiqueta del campo
                        html.Div(dcc.Input(id='identificacion', placeholder='Ingrese la identificación', type='text', className='form-control'), className='col-sm-9'),
                        html.Br(), html.Br(), html.Br()  # Añadimos saltos de línea para espaciar
                    ], className='form-group row'),

                    # Div para el campo de entrada del correo
                    html.Div([
                        html.Label("Correo:", className='col-sm-3 col-form-label'),  # Etiqueta del campo
                        html.Div(dcc.Input(id='correo', placeholder='Ingrese el correo', type='email', className='form-control'), className='col-sm-9'),
                        html.Br(), html.Br(), html.Br()  # Añadimos saltos de línea para espaciar
                    ], className='form-group row'),

                    # Div para el campo de entrada del celular
                    html.Div([
                        html.Label("Celular:", className='col-sm-3 col-form-label'),  # Etiqueta del campo
                        html.Div(dcc.Input(id='celular', placeholder='Ingrese el celular', type='tel', className='form-control'), className='col-sm-9'),
                        html.Br(), html.Br(), html.Br()  # Añadimos saltos de línea para espaciar
                    ], className='form-group row'),

                    # Div para el botón de agregar usuario
                    html.Div([
                        html.Button('Agregar Usuario', id='subirUsuario', n_clicks=0, className='btn btn-primary col-sm-3 offset-sm-3'),  # Botón para enviar el formulario
                    ], className='form-group row')
                ], className='container mt-4')  # Contenedor con margen superior
            ])
        ], md=6),  # La primera columna ocupa 6/12 de la fila

        # Segunda columna para mostrar el resultado de la inserción
        dbc.Col([
            html.H2(id="resultadoInsertado"),  # Encabezado donde se mostrará el resultado
        ], md=6),  # La segunda columna ocupa 6/12 de la fila
    ])
], 
# Estilo CSS aplicado al contenedor principal
style={
    'height': '100vh',  # Altura del contenedor ocupa toda la altura de la ventana
    'text-align': 'center',  # Texto centrado horizontalmente
    'justify-content': 'center',  # Contenido centrado horizontalmente
    'align-items': 'center',  # Contenido centrado verticalmente
})
