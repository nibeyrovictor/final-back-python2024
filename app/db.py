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

