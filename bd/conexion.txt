import mysql.connector

from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host = "localhost", 
        port=3306,
        user ="root",
        password="",
        db="prueba"
    )

    if conexion.is_connected():
        print("Conexión Exitosa")
        info = conexion.get_server_info()
        print("info del servidor: ",info)


except Error as ex:
    print("Error durante la conexion: ", ex)