#!/usr/bin/python3
"""
Write a script that deletes all State objects with a name containing the letter
a from the database hbtn_0e_6_usa:

- Your script should take 3 arguments: mysql username, mysql password and
database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state - from model_state import
Base, State
- Your script should connect to a MySQL server running on localhost at port3306
- Your code should not be executed when imported

delete(): https://www.geeksforgeeks.org/python-sqlalchemy-delete-multiple-rows/
"""
import sys
# importamos lo que creamos en el script model_state.py
from model_state import Base, State
# Import SQLAlchemy
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete  # delete method ()


if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    # Uso la funcion Session para abrir la sesion
    Session = sessionmaker(bind=engine)  # se une la sesion con el engine
    session = Session()  # creamos una instancia de "Session"

    # Se usa el metadata object para poder utilizar el nombre de la
    # tabla "states":
    table = Base.metadata.tables['states']

    # Uso del metodo delete() para borrar los estados que tengan la letra 'a':
    delet = table.delete().where(table.c.name.like('%a%'))
    # Guardar la nueva info actualizada:
    engine.execute(delet)

    # Close session that was opened
    session.close()
