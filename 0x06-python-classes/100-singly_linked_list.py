#!/usr/bin/python3
"""
Write a class: Node that defines a node of a singly linked list.
Write a class: SinglyLinkedList that defines a singly linked list.
"""


class Node:
    """This is a class for a Node"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        This is the getter func for a private instance attribute: data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set value for: data
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        return self.__data = value

    @property
    def next_node(self):
        """
        Getter func for a private instance attribute: next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set value for: next_node
        """
        if type(value) is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        return self.next_node = value


class SinlgyLinkedList:
    """
    Write a class that defines a singly linked list.
    """
    def __init__(self):
        """Initializes a singly linked list."""
        self.__head = None
