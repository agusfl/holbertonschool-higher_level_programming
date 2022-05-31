# Python - Inheritance:

Learning objectives:

* Why Python programming is awesome
* What is a superclass, baseclass or parentclass
* What is a subclass
* How to list all attributes and methods of a class or instance
* When can an instance have new attributes
* How to inherit class from another
* How to define a class with multiple base classes
* What is the default class every class inherit from
* How to override a method or attribute inherited from the base class
* Which attributes or methods are available by heritage to subclasses
* What is the purpose of inheritance
* What are, when and how to use isinstance, issubclass, type and super built-in functions

## Environment

* Language: Python
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [pycodestyle](https://pypi.org/project/pycodestyle/) - [Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
* Interpreter: python3 (version 3.8.5)

## Description of each file:

| Files          |Desription
|:----------------|:-------------------------------:|
|tests |Folder that holds tests suite cases.
|0-lookup.py |Function that returns the list of available attributes of an object --> use of ``dir``.
|1-my_list.py |Create a class named ``MyList`` that inherits from class ``list`` --> add a public instance method that prints the list sorted (ascending sort).
|2-is_same_class.py |Function that returns True if the object is **exactly** an instance of the specified class, otherwise return False.
|3-is_kind_of_class.py |Function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class, otherwise return False.
|4-inherits_from.py |Function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class, otherwise return False.
|5-base_geometry.py |Create an empty class named ``BaseGeometry``.
|6-base_geometry.py |Add a public instance method named ``area`` that raises an exception with the message: "area() is not implemented".
|7-base_geometry.py |Add a public instance method named ``integer_validator`` that validates the argument **value**.
|8-rectangle.py |Create a class ``Rectangle`` that inherits from class ``BaseGeometry``.
|9-rectangle.py |Add __str__ method with the following description: [Rectangle] <width>/<height>.
|10-square.py |Create a class ``Square`` that inherits from class ``Rectangle``.
|11-square.py |Add __str__ method with the following description: [Square] <width>/<height>.
|100-my_int.py |Create a class ``MyInt`` that inherits from class ``int`` --> invert the meaning of the == (equal) operator and the != (not equal) operator.
|101-add_attribute.py |Function that adds a new attribute to an object if it is possible --> use of: setattr() method.

## Authors

* [Agustin Flom](https://github.com/agusfl)
