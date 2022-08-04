#!/usr/bin/python3
"""
Write a script that prints the first State object from the database
hbtn_0e_6_usa:
- Your script should take 3 arguments: mysql username, mysql password and
database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state - from model_state import
Base, State
- Your script should connect to a MySQL server running on localhost at port3306
- The state you display must be the first in states.id
- You are not allowed to fetch all states from the database before displaying
the result
- The results must be displayed as they are in the example below
- If the table states is empty, print Nothing followed by a new line
- Your code should not be executed when imported
"""
import sys
# importamos lo que creamos en el script model_state.py
from model_state import Base, State
# Import SQLAlchemy
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    # Uso la funcion Session para abrir la sesion
    Session = sessionmaker(bind=engine)  # se une la sesion con el engine
    session = Session()  # creamos una instancia de "Session"

    cont = 0
    # Se hace un for para imprimir todos los objetos de la tabla 'state'
    for state in session.query(State).order_by(State.id).all():
        cont += 1  # creo un contador para ver cuando imprimir
        if cont == 1:  # si cont es 1 imprimimos
            print(f"{state.id}: {state.name}")
        if cont == 0:  # si la tabla states esta vacia imprimimos Nothing
            print("Nothing")

    # Se cierra la sesion
    session.close()
