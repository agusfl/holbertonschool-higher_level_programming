#!/usr/bin/python3
"""
Write a script that creates the State “California” with the City “San Francisco
” from the database hbtn_0e_100_usa: (100-relationship_states_cities.py):

- Your script should take 3 arguments: mysql username, mysql password and
database name
- You must use the module SQLAlchemy
- Your script should connect to a MySQL server running on localhost at port3306
- You must use the cities relationship for all State objects
- Your code should not be executed when imported

Info backref: https://programmerclick.com/article/82401238841/
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

    # Create object State to add to hbtn_0e_100_usa
    California = State(name="California")
    # Create object city to add to hbtn_0e_100_usa
    SanFrancisco = City(name="San Francisco")

    # Se agrega en el estado california la ciudad San Francisco usando la
    # relationship "city"
    California.cities.append(SanFrancisco)

    # Add objects to each table
    session.add(California)
    session.add(SanFrancisco)

    # Save changes
    session.commit()

    # Close session that was opened
    session.close()
