#!/usr/bin/python3
"""This module create a linked list"""


class Node:
    """This class represents a node"""

    def __init__(self, data, next_node=None):
        """Initialise data

        Parameters:
        ----------
        data : int : value of the node
        next_node : next_node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter to access of the node value

        Return
        ------
        int : value of the node
        """
        return self.__data

    @property
    def next_node(self):
        """getter to access of the next node

        Return
        ------
        next_node

        """
        return self.__next_node

    @data.setter
    def data(self, value):
        """
        setter to update the Node value

        Raise
        -----
        TypeError : if value is not an int
        """
        if not (isinstance(value, int)):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        """
        setter to update the next_node

        Raise
        -----
        TypeError : if value is not a Node
        """
        if (value is not None and not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """This class define a singly linkedList"""

    def __init__(self):
        """
        Initialise data
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a node in ascending order

        Parameter
        ---------
        value : int : value of the node
        """
        new_node = Node(value)
        current = self.__head
        if (current is None):
            self.__head = new_node
        elif (current.next_node is None):
            if current.data >= value:
                new_node.next_node = current
                self.__head = new_node
            else:
                current.next_node = new_node
        else:
            while (current):
                if (current.data >= value):
                    new_node.next_node = current
                    self.__head = new_node
                    break
                elif (current.next_node is not None and current.next_node.data >= value):
                    new_node.next_node = current.next_node
                    current.next_node = new_node
                    break
                elif (current.next_node is not None):
                    current.next_node = new_node
                    new_node.next_node = None
                    break
                current = current.next_node

    def __str__(self):
        """
        Print the linked list

        Return
        ------
        The linked list in the str format
        """
        result = ""
        node = self.__head
        while node:
            result += str(node.data)
            if (node.next_node is None):
                break
            result += "\n"
            node = node.next_node
        return result
