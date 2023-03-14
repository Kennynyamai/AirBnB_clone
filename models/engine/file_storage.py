#!/usr/bin/python3
import json
"""Module for FileStorage class."""

class FileStorage:
    def __init__(self):
        self.__file_path = ""
        self.__objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects = obj["__class__.__name__.id"]
    
    def save(self):
        json.dump(self.__objects, self.__file_path)

    def reload(self):
        if len(self.__file_path) > 0:
            data = open(self.__file_path,)
            self.__objects = json.load(data)