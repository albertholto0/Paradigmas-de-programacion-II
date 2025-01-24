from mysql.connector import (connection)

db_unsij = connection.MySQLConnection(
    host = "localhost",
    user = "root",
    password = "root",
    database = "unsij_python"
)

cursor = db_unsij.cursor()
sql_query = "INSERT INTO alumnos(nombre_completo,matricula,id_grupo) values(%s, %s, %s)"
values = ("Prueba","123",2)

cursor.execute(sql_query,values)
db_unsij.commit()
db_unsij.close()