#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
- Your script should take 4 arguments: mysql username, mysql password, database
name and state name searched (no argument validation needed)
- You must use the module MySQLdb (import MySQLdb)
- Your script should connect to a MySQL server running on localhost at port3306
- You must use format to create the SQL query with the user input
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
        stateName_search = argv[4]  # string to be searched

        # Defino la variable "conn" para establecer la conexion usando la
        # funcion "connect" de MySQLdb
        conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_user,
                               passwd=mysql_password, db=database_name,
                               charset="utf8")

        # Definimos nuestra variable "conn" que usa la funcion "cursor" para
        # poder hacer consultas de SQL
        cur = conn.cursor()
        # Escibimos la SQL query usando la funcion "execute":
        # If you want to spread strings over multiple lines, you also have the
        # option of escaping a return with a \:
        cur.execute(f"SELECT *FROM states WHERE name LIKE BINARY '{stateName_search}'\
                    ORDER BY id ASC")
        # Se guardan los resultados de la query que ejecutamos con "execute".

        # Usando la funcion "fetchall" cargamos los resultados en la variable
        # "query_rows"
        query_rows = cur.fetchall()
        # Imprimimos los resultados usando un for y un print
        for row in query_rows:
            print(row)
        # Cerramos las conexiones
        cur.close()
        conn.close()

    except (Exception) as errors:
        print("There was an error")
