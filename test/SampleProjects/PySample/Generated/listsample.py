import json
from objectlist import ObjectList
#####################################################################################
# This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)  #
# Modifications to this file will be lost the next time you run the tool.           #
# Date: 2015-01-06                                                                  #
#####################################################################################


class ListSample:
    def __init__(self):
        self._int_list = []
        self._float_list = []
        self._string_list = []
        self._object_list = []

    @classmethod
    def load(cls, json_obj):
        """:type json_obj: dict
           :rtype: ListSample"""
        obj = ListSample()
        obj._int_list = []
        for item in json_obj["intList"]:
            obj._int_list.append(item)
        obj._float_list = []
        for item in json_obj["floatList"]:
            obj._float_list.append(item)
        obj._string_list = []
        for item in json_obj["stringList"]:
            obj._string_list.append(item)
        obj._object_list = []
        for item in json_obj["objectList"]:
            obj._object_list.append(ObjectList.load(item))
        return obj

    @property
    def int_list(self):
        """:rtype: list of [int]"""
        return self._int_list
    @int_list.setter
    def int_list(self, value):
        """:type value: list of [int]
           :rtype: None"""
        self._int_list = value

    @property
    def float_list(self):
        """:rtype: list of [float]"""
        return self._float_list
    @float_list.setter
    def float_list(self, value):
        """:type value: list of [float]
           :rtype: None"""
        self._float_list = value

    @property
    def string_list(self):
        """:rtype: list of [str]"""
        return self._string_list
    @string_list.setter
    def string_list(self, value):
        """:type value: list of [str]
           :rtype: None"""
        self._string_list = value

    @property
    def object_list(self):
        """:rtype: list of [ObjectList]"""
        return self._object_list
    @object_list.setter
    def object_list(self, value):
        """:type value: list of [ObjectList]
           :rtype: None"""
        self._object_list = value


    def to_json(self):
        """:rtype: str"""
        return ListSample.JsonEncoder().encode(self)

    class JsonEncoder(json.JSONEncoder):
        def default(self, obj):
            d = {
                'intList': [],
                'floatList': [],
                'stringList': [],
                'objectList': [],
            }
            for item in obj.int_list:
                d['family'].append(item)

            for item in obj.float_list:
                d['family'].append(item)

            for item in obj.string_list:
                d['family'].append(item)

            for item in obj.object_list:
                d['family'].append(item.to_json())

            return d