#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
- Your script should take 4 arguments: mysql username, mysql password, database
name and state name (SQL injection free!)
- You must use the module MySQLdb (import MySQLdb)
- Your script should connect to a MySQL server running on localhost at port3306
- Results must be sorted in ascending order by cities.id
- You can use only execute() once
- The results must be displayed as they are in the example below
- Your code should not be executed when imported

Task muy similar a la anterior pero agregando un cuarto argumento en linea
el cual nos va a indicar el estado del cual queremos mostrar todas las ciudades
que esten en ese estado.
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
        # Uso el %s para que el codigo no sea vulnerable a SQL injections
        cur.execute("SELECT cities.name AS name \
                    FROM cities INNER JOIN states ON \
                    cities.state_id = states.id \
                    WHERE states.name = %s ORDER BY cities.id",
                    (stateName_search,))
        # Se guardan los resultados de la query que ejecutamos con "execute"
        # usando la funcion "fetchall"
        query_rows = cur.fetchall()
        cont = 0  # creo una variable contadora para ver cuando poner la coma
        lenght = len(query_rows)  # Obtengo la cantidad de datos
        # Imprimimos los resultados usando un for y un print
        for rows in query_rows:
            for row in rows:
                print(row, end='')
                cont = cont + 1
            if lenght != cont:  # Poner coma siempre y cuando no sea el ultimo
                print(', ', end='')
        print()
        # Cerramos las conexiones
        cur.close()
        conn.close()

    except (Exception) as errors:
        print("There was an error")
