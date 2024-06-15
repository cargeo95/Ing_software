# Importamos el módulo html de Dash (no se utiliza en esta función específica)
from dash import html

# Importamos el objeto Error del conector de MySQL para manejar excepciones
from mysql.connector import Error

# Función para insertar un usuario en la base de datos
def insertarUsuarioController(connection, nombre, identificacion, correo, celular):
    try:
        # Creamos un cursor para ejecutar comandos SQL
        cursor = connection.cursor()
        
        # Definimos la consulta SQL para insertar un nuevo usuario
        query = """
        INSERT INTO usuarios (nombre, identificacion, correo, celular)
        VALUES (%s, %s, %s, %s)
        """
        
        # Asignamos los valores que se van a insertar en la consulta
        values = (nombre, identificacion, correo, celular)
        
        # Ejecutamos la consulta con los valores proporcionados
        cursor.execute(query, values)
        
        # Confirmamos (hacemos commit) los cambios en la base de datos
        connection.commit()
        
        # Retornamos un mensaje de éxito si la inserción fue exitosa
        return "Insertado exitosamente"
    except Error as e:
        # En caso de error, revertimos (hacemos rollback) los cambios
        connection.rollback()
        
        # Retornamos un mensaje de error
        return "Error al insertar el usuario"
    finally:
        # Finalmente, cerramos la conexión si está abierta y conectada
        if connection is not None and connection.is_connected():
            connection.close()


# Función para leer usuarios desde la base de datos
def leerUsuariosController(connection):
    try:
        # Creamos un cursor para ejecutar comandos SQL
        cursor = connection.cursor()
        # Definimos la consulta SQL para seleccionar todos los usuarios
        query = "SELECT nombre, identificacion, correo, celular FROM usuarios"
        # Ejecutamos la consulta
        cursor.execute(query)
        # Obtenemos todos los registros
        usuarios = cursor.fetchall()
        
        # Retornamos los usuarios obtenidos
        return usuarios
    except Error as e:
        # Aquí podrías manejar el error de alguna manera específica si lo deseas
        return None
    finally:
        # Finalmente, cerramos el cursor y la conexión si están abiertos y conectados
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

