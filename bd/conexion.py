# Importamos el conector de MySQL y el objeto de Error para manejar excepciones
import mysql.connector
from mysql.connector import Error

# Función para configurar y establecer la conexión a la base de datos
def conexion():
    connection = None  # Inicializamos la variable de conexión como None
    try:
        # Intentamos establecer la conexión con los parámetros de configuración
        connection = mysql.connector.connect(
            host="localhost",  # Dirección del servidor de la base de datos
            user="root",  # Nombre de usuario para la conexión
            password="",  # Contraseña para la conexión
            database="parqueaderoautoscolombia"  # Nombre de la base de datos
        )
        # Verificamos si la conexión se ha establecido correctamente
        if connection.is_connected():
            return connection  # Retornamos el objeto de conexión
                    
    except Error as e:
        # Capturamos cualquier error que ocurra durante la conexión y lo imprimimos
        print(f"Error al conectar a MySQL: {e}")
