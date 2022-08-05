#!/usr/bin/python3
"""
Next, write a script 14-model_city_fetch_by_state.py that prints all City
objects from the database hbtn_0e_14_usa:

- Your script should take 3 arguments: mysql username, mysql password and
database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state - from model_state import
Base, State
- Your script should connect to a MySQL server running on localhost at port3306
- Results must be sorted in ascending order by cities.id
- Results must be display as they are in the example below (<state name>:
(<city id>) <city name>)
- Your code should not be executed when imported

Info join: https://overiq.com/sqlalchemy-101/crud-using-sqlalchemy-orm/
"""
import sys
# importamos lo que creamos en el script model_state.py
from model_state import Base, State
# Import SQLAlchemy
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    # Uso la funcion Session para abrir la sesion
    Session = sessionmaker(bind=engine)  # se une la sesion con el engine
    session = Session()  # creamos una instancia de "Session"

    # Se hace la query para sacar los datos que se pidan:
    data = session.query(State.name, City.id, City.name).join(City).all()
    # Se imprime la data en el formato que nos piden
    # state_city devuelve una tupla, accedo a cada parametro de la misma:
    # print(data) --> te muestra lo que se trae en data que es una lista.
    for state_city in data:
        print(f"{state_city[0]}: ({state_city[1]}) {state_city[2]}")

    # Close session that was opened
    session.close()
