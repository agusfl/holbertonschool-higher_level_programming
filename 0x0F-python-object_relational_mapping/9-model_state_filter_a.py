#!/usr/bin/python3
"""
Write a script that lists all State objects that contain the letter a from the
database hbtn_0e_6_usa:

- Your script should take 3 arguments: mysql username, mysql password and
database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state - from model_state import
Base, State
- Your script should connect to a MySQL server running on localhost at port3306
- Results must be sorted in ascending order by states.id
- The results must be displayed as they are in the example below
- Your code should not be executed when imported

filter() and like()
https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_filter_operators.htm
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

    # Se hace un for para imprimir todos los objetos de la tabla 'state'
    for state in session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all():
        print(f"{state.id}: {state.name}")
    # Se cierra la sesion
    session.close()
