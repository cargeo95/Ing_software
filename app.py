# Importamos las librerías necesarias de Dash y otros módulos
from dash import Dash, html, Input, Output, State,callback_context
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import re

# Importamos el diseño de la interfaz desde el módulo frontend
from frontend.layout import layout

# Importamos funciones relacionadas con la base de datos
from bd.conexion import conexion
from bd.usuariosController import insertarUsuarioController, leerUsuariosController

# Creamos una instancia de la aplicación Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Configuramos el título de la aplicación
app.title = 'Aplicación Registro de Carros'

# Establecemos el diseño de la aplicación utilizando el layout importado
app.layout = layout

# Definimos un callback para manejar la inserción de un nuevo usuario
@app.callback(
    Output('resultadoInsertado', 'children'),  # El output es el contenido del componente con ID 'resultadoInsertado'
    Input('subirUsuario', 'n_clicks'),  # El input es el número de clics en el botón con ID 'subirUsuario'
    State('nombre', 'value'),  # El estado del valor del campo de texto con ID 'nombre'
    State('identificacion', 'value'),  # El estado del valor del campo de texto con ID 'identificacion'
    State('correo', 'value'),  # El estado del valor del campo de texto con ID 'correo'
    State('celular', 'value')  # El estado del valor del campo de texto con ID 'celular'
)
def registrarUsuario(n_clicks, nombre, identificacion, correo, celular):
    # Si el botón no ha sido clickeado, prevenimos la actualización
    if n_clicks is None:
        raise PreventUpdate
    
    # Verificamos que todos los campos estén llenos
    if not nombre or not identificacion or not correo or not celular:
        return "Ingrese los valores faltantes"
    
    # Verificamos que el campo 'identificacion' contenga solo números
    if not re.fullmatch(r'\d+', identificacion):
        return "El campo identificación solo debe contener números"
    
    # Verificamos que el campo 'celular' contenga solo números
    if not re.fullmatch(r'\d+', celular):
        return "El campo celular solo debe contener números"
    
    # Verificamos que el campo 'celular' tenga exactamente 10 dígitos
    if not re.fullmatch(r'\d{10}', celular):
        return "El campo celular debe contener exactamente 10 números"
    
    # Establecemos la conexión a la base de datos
    connection = conexion()
    
    # Insertamos el nuevo usuario en la base de datos y obtenemos el resultado
    result = insertarUsuarioController(connection, nombre, identificacion, correo, celular)
    
    # Devolvemos el resultado de la operación
    return result


# Callback para actualizar los datos de la tabla con los usuarios desde la base de datos
@app.callback(
    Output('resultadoUsuarios', 'data'),
    Input('resultadoUsuarios', 'loading_state')  # Cualquier input que dispare la actualización de la tabla
)
def update_table_data(input_value):
    # Leer los usuarios desde la base de datos al actualizar la tabla
    connection = conexion()
    if connection:
        usuarios = leerUsuariosController(connection)
        if usuarios:
            data = [{'nombre': nombre, 'identificacion': identificacion, 'correo': correo, 'celular': celular}
                    for nombre, identificacion, correo, celular in usuarios]
            return data
    return []


# Ejecutamos la aplicación en modo debug si este script es el principal
if __name__ == "__main__":
    app.run_server(debug=True)
