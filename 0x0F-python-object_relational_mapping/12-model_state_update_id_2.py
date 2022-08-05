#!/usr/bin/python3
"""
Write a script that changes the name of a State object from the database
hbtn_0e_6_usa:

- Your script should take 3 arguments: mysql username, mysql password and
database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state - from model_state import
Base, State
- Your script should connect to a MySQL server running on localhost at port3306
- Change the name of the State where id = 2 to New Mexico
- Your code should not be executed when imported

Info Update: https://www.geeksforgeeks.org/sqlalchemy-core-update-statement/
Base.metadata:
https://stackoverflow.com/questions/6473925/sqlalchemy-getting-a-list-of-tables
.c: https://docs.sqlalchemy.org/en/14/core/selectable.html#sqlalchemy.sql.
expression.FromClause.columns
"""
import sys
# importamos lo que creamos en el script model_state.py
from model_state import Base, State
# Import SQLAlchemy
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update


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

    # Uso del metodo udpate():
    upd = update(table)
    upd = upd.where(table.c.id == 2)
    upd = upd.values(name="New Mexico")
    # Guardar la nueva info actualizada:
    engine.execute(upd)

    # Close session that was opened
    session.close()
