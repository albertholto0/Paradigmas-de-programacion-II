from mysql.connector import (connection)

unsij_db = connection.MySQLConnection(
    host = "localhost",
    user = "root",
    password = "root",
    database = "unsij_python"
)

cursor = unsij_db.cursor()
cursor.execute("select * from carreras|")
alumnos = cursor.fetchall()

for alumno in alumnos:
    print(alumno)

unsij_db.close()