# instalar pymysql -> pip install pymysql
# importar pymysql / SQLachemy / dbmysql

import pymysql

#conexion base de datos
def conectarMysql():
    host="localhost"
    user="root"
    password=""
    db="argentur"
    return pymysql.connect(host=host,user=user,password=password,database=db)

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

