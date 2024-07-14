import mysql.connector

# Conexion a la base de datos
def conectarMysql():
    conexion = mysql.connector.connect(
        # host='localhost',
        # user='root',
        # password='',
        # database='argentur'
                
        host='Nibpos.mysql.pythonanywhere-services.comt',
        user='Nibpos',
        password='Nyp-2020DG5415cac',
        database='Nibpos$argentSDFTur'
    )
    return conexion

# Example of using the connection
try:
    conn = conectarMysql()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")
    results = cursor.fetchall()
    
    for row in results:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
