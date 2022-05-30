#!/usr/bin/python3
"""
Create a class MyInt that inherits from int class.
"""


class MyInt(int):
    """
    Sub class of int named "MyInt" that inverts == for !=
    """
    def __init__(self, number):
        """Initialize number"""
        self.number = number

    def __eq__(self, other):
        """Change equal operator for not equal"""
        return self.number != other

    def __ne__(self, other):
        """Change not equal operator for equal operator"""
        return self.number == other
