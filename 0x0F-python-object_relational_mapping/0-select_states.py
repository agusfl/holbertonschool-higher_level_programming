#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa:
- Your script should take 3 arguments: mysql username, mysql password and
database name (no argument validation needed)
- You must use the module MySQLdb (import MySQLdb)
- Your script should connect to a MySQL server running on localhost at port3306
- Results must be sorted in ascending order by states.id
- Results must be displayed as they are in the example below
- Your code should not be executed when imported
"""

# No se tiene que ejecutar el codigo cuando el modulo es importado
if __name__ == "__main__":
    # Importo "argv" del modulo "sys" para usar los command-line arguments
    from sys import argv
    # Importo el modulo "MySQLdb" para poder usar SQL en Python
    import MySQLdb

    # Uso un try y un except por si surgen errores para que no se crashee
    # nuestro programa.
    try:
        # Guardo los comandos command-line arguments en variables para que
        # nuestro codigo sea generico a lo que el usuario pase como argumentos
        mysql_user = argv[1]
        mysql_password = argv[2]
        database_name = argv[3]

        # Defino la variable "conn" para establecer la conexion usando la
        # funcion "connect" de MySQLdb
        conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_user,
                               passwd=mysql_password, db=database_name,
                               charset="utf8")

        # Definimos nuestra variable "conn" que usa la funcion "cursor" para
        # poder hacer consultas de SQL
        cur = conn.cursor()
        # Escibimos la SQL query usando la funcion "execute":
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        # Se guardan los resultados de la query que ejecutamos con "execute"
        # usando la funcion "fetchall"
        query_rows = cur.fetchall()
        # Imprimimos los resultados usando un for y un print
        for row in query_rows:
            print(row)
        # Cerramos las conexiones
        cur.close()
        conn.close()

    except (Exception) as errors:
        print("There was an error")
