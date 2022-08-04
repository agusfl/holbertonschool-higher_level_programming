#!/usr/bin/python3
"""
Write a script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa:

- Your script should take 4 arguments: mysql username, mysql password, database
name and state name to search (SQL injection free)
- You must use the module SQLAlchemy
- You must import State and Base from model_state - from model_state import
Base, State
- Your script should connect to a MySQL server running on localhost at port3306
- You can assume you have one record with the state name to search
- Results must display the states.id
- If no state has the name you searched for, display Not found
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

    name_search = sys.argv[4]  # string to be searched

    # Se crea una variable data donde se guarda el resultado de la query:
    data = session.query(State).filter(State.name == name_search).first()
    if (data):
        print(f"{data.id}")
    else:
        print("Not found")
    # Se cierra la sesion
    session.close()
