#!/usr/bin/python3
"""
Defines a Base module.
"""
import json


class Base:
    """Initialize Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): list of dict respersentaion.

        Returns:
            (str): Json represantation
        """
        if list_dictionaries is None:
            list_dictionaries = "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file.

        Args:
            cls: class
            list_objs (list): is list of instances.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        li = []
        if list_objs is not None:
            for i in list_objs:
                li.append(cls.to_dictionary(i))

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(li))

    @staticmethod
    def from_json_string(json_string):
        """Represent json string"""
        if json_string is None or json_string is "":
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances."""
        try:
            filename = cls.__name__ + ".json"
            with open(filename, 'r') as f:
                json_list = cls.from_json_string(f.read())
                obj_list = []
                for j in obj_list:
                    obj_list.append(cls.create(**j))
                return obj_list
        except:
            return []
