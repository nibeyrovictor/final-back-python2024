impoot pymysql
from db import conectarMysql

def obtenerUsuarios():
    # conexion mysql
    conexion = conectarMysql()
    usuarios = []
    with conexion.cursor() as cursor:
        sql = "SELECT * FROM usuarios"
    # consulta
        cursor.execute(sql)
        usuarios = cursor.fetchall()
    # return resultados
        return usuarios    

