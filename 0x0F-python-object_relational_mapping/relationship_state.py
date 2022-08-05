#!/usr/bin/python3
"""
Write a python file that contains the class definition of a State and an
instance Base = declarative_base():
* State class:
- inherits from Base Tips
- links to the MySQL table states
- class attribute id that represents a column of an auto-generated, unique
integer, can’t be null and is a primary key
- class attribute name that represents a column of a string with maximum 128
characters and can’t be null
* You must use the module SQLAlchemy
* Your script should connect to a MySQL server running on localhost at port3306
* WARNING: all classes who inherit from Base must be imported before calling
Base.metadata.create_all(engine)

Info para esta task:
https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/basic_use.html
Mas info: https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_declaring_
mapping.htm#:~:text=A%20base%20class%20stores%20a,used%20to%20create%20base%20class.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# The declarative_base() function is used to create base class:
Base = declarative_base()


# Creamos la clase State que hereda de Base
class State(Base):
    """
    State class inherit from Base
    """
    # creamos la tabla "states" la clase State va a estar asociada a esta tabla
    __tablename__ = 'states'
    # Se crean las variables que va a tener la tabla "states":
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    city = relationship('City', backref="state")
