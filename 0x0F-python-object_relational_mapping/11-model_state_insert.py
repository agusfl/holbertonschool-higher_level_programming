#!/usr/bin/python3
"""
Write a script that adds the State object “Louisiana” to the database
hbtn_0e_6_usa:

- Your script should take 3 arguments: mysql username, mysql password and
database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state - from model_state import
Base, State
- Your script should connect to a MySQL server running on localhost at port3306
- Print the new states.id after creation
- Your code should not be executed when imported

How to add data to a database using sqlalchemy in python:
https://www.youtube.com/watch?v=T6Q6bsv05To&ab_channel=JerinJose
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

    # Create object to add to the database --> hbtn_0e_6_usa
    Louisiana = State(id=6, name="Louisiana")
    # Print id after creation of the object:
    print(Louisiana.id)

    # Add object to table "states"
    session.add(Louisiana)
    # Save new info in table
    session.commit()

    # Close session that was opened
    session.close()
