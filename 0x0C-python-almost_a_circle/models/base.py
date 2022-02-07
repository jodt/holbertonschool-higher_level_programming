#!/usr/bin/python3
"""
This module is the base for all the classes
"""
import json


class Base:
    """
    this class manage the id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialise data

        Parameters:
        -----------
        id (int) : id
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of
        dictionaries list

        Parameter:
        ----------
        list_dictionnaries (list) : list of dictionnaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            json_str = "["
            for elt in list_dictionaries:
                json_str += json.dumps(elt)
                json_str += ", "
            json_str = json_str[:-2] + "]"
        return json_str

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation

        Parameter:
        ----------
        json_string (str) : JSON str
        """
        if json_string is None or len(json_string) == 0:
            return list()
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of objetcs list
        to a file

        Parameter:
        ----------
        list_objs : objects list
        """
        filename = cls.__name__+".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string(
                    [elt.to_dictionary() for elt in list_objs]))

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            create_instance = cls(3, 5)
        else:
            create_instance = cls(3)
        create_instance.update(**dictionary)
        return create_instance

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = cls.__name__ + ".json"
        instances_result = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                read_file = f.read()
            instances_list = cls.from_json_string(read_file)
            for elt in instances_list:
                instances_result.append(cls.create(**elt))
            return instances_result
        except Exception:
            return instances_result
