import pymysql
from db import conectarMysql


#Contacto formulario
def guardar_contacto(nombre, apellido, comentario, mail):
    conexion = conectarMysql()
    with conexion.cursor() as cursor:
        query = "INSERT INTO contacto (nombre, apellido, comentario, mail) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (nombre, apellido, comentario, mail))
        conexion.commit()
        conexion.close()
        return "Data saved successfully!"  # Or return a success message
