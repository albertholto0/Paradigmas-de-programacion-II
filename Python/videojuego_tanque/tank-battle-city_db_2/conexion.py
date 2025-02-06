from mysql.connector import pooling, Error

class Conexion:
    pool = None

    @classmethod
    def get_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    host="172.25.3.194",
                    user="albert_redes",
                    password="root",
                    database="tank_battle",
                    pool_name="tank_battle_pool",
                    pool_size=5
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
