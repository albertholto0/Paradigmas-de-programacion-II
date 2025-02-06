from mysql.connector import pooling, Error

class Conexion:
    pool = None

    @classmethod
    def get_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    host = "localhost",
                    user = "root",
                    password = "root",
                    database = "unsij_python",
                    pool_name = "db_unsij_python_pool",
                    pool_size = 5
                )
                print("Pool creado")
                return cls.pool
            except Error as e:
                print(f"Error al crear el pool... | {e}")
        else:
            return cls.pool

    @classmethod
    def get_connection(cls):
        return cls.get_pool().get_connection()

if __name__ == "__main__":
    # pool = Conexion.get_pool()
    # print(pool)

    cn1 = Conexion.get_connection()
    print(cn1)

    cursor = cn1.cursor()
    cursor.execute("select * from carreras")
    alumnos = cursor.fetchall()

    for alumno in alumnos:
        print(alumno)

    # my_cursor = cnl.cursor()