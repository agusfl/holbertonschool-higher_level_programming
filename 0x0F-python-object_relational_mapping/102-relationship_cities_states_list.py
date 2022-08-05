#!/usr/bin/python3
"""
Write a script that lists all City objects from the database hbtn_0e_101_usa:

- Your script should take 3 arguments: mysql username, mysql password and
database name
- You must use the module SQLAlchemy
- Your script should connect to a MySQL server running on localhost at port3306
- You must use only one query to the database
- You must use the state relationship to access to the State object linked to
the City object
- Results must be sorted in ascending order by cities.id
- Results must be displayed as they are in the example below
- Your code should not be executed when imported
"""
import sys
# importamos lo que creamos en el script model_state.py
from relationship_state import Base, State
from relationship_city import City  # Usamos relationship_city
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

    # Se hace la query para sacar los datos que se piden:
    data = session.query(
        State.name, City.id, City.name).join(City).order_by(City.id).all()
    # Hago un for muy similar a lo que hice en la task 14
    for state_city in data:
        print(f"{state_city[1]}: {state_city[2]} -> {state_city[0]}")

    # Close session that was opened
    session.close()
