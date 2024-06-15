from dash import html , dcc,dash_table
import dash_bootstrap_components as dbc


inicio = dbc.Container([
    html.Br(),html.Br(),
    html.H3("Inicio"),
    html.Hr(),
    dash_table.DataTable(
        id="resultadoUsuarios",
        columns=[
            {'name': 'Nombre', 'id': 'nombre'},
            {'name': 'Identificación', 'id': 'identificacion'},
            {'name': 'Correo', 'id': 'correo'},
            {'name': 'Celular', 'id': 'celular'}
        ],
        data=[]
    )
    
])