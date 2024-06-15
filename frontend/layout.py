# Importamos las librerías necesarias de Dash y otros módulos
from dash import html , dcc,dash_table
import dash_bootstrap_components as dbc

# Importamos los diferentes módulos para cada una de las pestañas
from .tabs.usuarios import usuarios
from .tabs.inicio import inicio
from .tabs.vehiculo import vehiculo
from .tabs.gestion import gestion

# Definimos el diseño (layout) principal de la aplicación
layout = dbc.Container([
    html.Br(),  # Añadimos un salto de línea para espaciar los elementos
    html.H1("Parqueadero Autos Colombia"),  # Encabezado principal de la aplicación
    html.Hr(),  # Línea horizontal para separar el encabezado del resto del contenido
    dcc.Tabs(
        id="tab",  # ID del componente Tabs para referencia en callbacks
        value="Usuario",  # Valor inicial seleccionado de las pestañas
        children=[
            # Definición de la pestaña "Inicio"
            dcc.Tab(
                inicio,  # Contenido de la pestaña importado del módulo correspondiente
                label="Inicio",  # Etiqueta que se mostrará en la pestaña
                value="Inicio"  # Valor de la pestaña para identificación
            ),
            # Definición de la pestaña "Usuarios"
            dcc.Tab(
                usuarios,  # Contenido de la pestaña importado del módulo correspondiente
                label="Usuario",  # Etiqueta que se mostrará en la pestaña
                value="Usuario"  # Valor de la pestaña para identificación
            ),
            # Definición de la pestaña "Vehículo"
            dcc.Tab(
                vehiculo,  # Contenido de la pestaña importado del módulo correspondiente
                label="Vehiculo",  # Etiqueta que se mostrará en la pestaña
                value="Vehiculo"  # Valor de la pestaña para identificación
            ),
            # Definición de la pestaña "Gestión de pago"
            dcc.Tab(
                gestion,  # Contenido de la pestaña importado del módulo correspondiente
                label="GESTION DE PAGO",  # Etiqueta que se mostrará en la pestaña
                value="Gestion"  # Valor de la pestaña para identificación
            ),
        ]
    )
],
# Estilo CSS aplicado al contenedor principal
style={
    'height': '100vh',  # Altura del contenedor ocupa toda la altura de la ventana
    'text-align': 'center',  # Texto centrado horizontalmente
    'justify-content': 'center',  # Contenido centrado horizontalmente
    'align-items': 'center',  # Contenido centrado verticalmente
})
