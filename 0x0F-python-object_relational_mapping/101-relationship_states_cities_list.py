#!/usr/bin/python3
"""
Write a script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa:

- Your script should take 3 arguments: mysql username, mysql password and
database name
- You must use the module SQLAlchemy
- The connection to your MySQL server must be to localhost on port 3306
- You must only use one query to the database
- You must use the cities relationship for all State objects
- Results must be sorted in ascending order by states.id and cities.id
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

    # Creamos las tablas que se importan en el script, en este caso 'states'
    Base.metadata.create_all(engine)
    # Uso la funcion Session para abrir la sesion
    Session = sessionmaker(bind=engine)  # se une la sesion con el engine
    session = Session()  # creamos una instancia de "Session"

    # Se hace la query para sacar los datos que se pidan:
    data = session.query(State).order_by(State.id).all()

    # print(data):te muestra los objetos que se traen de la query de mas arriba
    # Para ver lo que esta en el primer lugar de data: print(data[0].name)
    # Se imprime la data en el formato que nos piden usando la relacion
    # establecida en relationship_state.py -> "cities"
    for states in data:
        print(f"{states.id}: {states.name}")
        for cities in states.cities:  # accedo a cada ciudad dentro del estado
            print(f"    {cities.id}: {cities.name}")

    # Close session that was opened
    session.close()
