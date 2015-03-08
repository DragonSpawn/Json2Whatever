import json
from objectlist import ObjectList
#####################################################################################
# This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)  #
# Modifications to this file will be lost the next time you run the tool.           #
# Date: 2015-03-08                                                                  #
#####################################################################################


class ListSample(object):
    def __init__(self):
        self._int_list = []
        self._float_list = []
        self._string_list = []
        self._object_list = []

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

    class JsonFactory():
        def __init__(self):
            pass

        @staticmethod
        def to_json(obj):
            """
            Takes an ListSample or a list of ListSample and returns a json string representation of itn            :rtype: str
            """
            return ListSample.JsonFactory.JsonEncoder().encode(obj)

        class JsonEncoder(json.JSONEncoder):
            def default(self, obj):
                if obj is None:
                    return None
                d = {
                    'intList': [],
                    'floatList': [],
                    'stringList': [],
                    'objectList': [],
                }
                for item in obj.int_list:
                    d['intList'].append(item)

                for item in obj.float_list:
                    d['floatList'].append(item)

                for item in obj.string_list:
                    d['stringList'].append(item)

                for item in obj.object_list:
                    d['objectList'].append(ObjectList.JsonFactory.JsonEncoder().default(item))

                return d

        @staticmethod
        def from_json_array(json_array):
            """
            :type json_array: list
            :rtype: list of [ListSample]
            """
            result = []
            for obj in json_array:
                result.append(ListSample.JsonFactory.from_json(obj))
            return result

        @staticmethod
        def from_json(json_obj):
            """:type json_obj: dict
               :rtype: ListSample"""
            if json_obj is None:
                return None
            obj = ListSample()

            if "intList" in json_obj:
                obj._int_list = []
                for item in json_obj["intList"]:
                    obj._int_list.append(item)
            if "floatList" in json_obj:
                obj._float_list = []
                for item in json_obj["floatList"]:
                    obj._float_list.append(item)
            if "stringList" in json_obj:
                obj._string_list = []
                for item in json_obj["stringList"]:
                    obj._string_list.append(item)
            if "objectList" in json_obj:
                obj._object_list = []
                for item in json_obj["objectList"]:
                    obj._object_list.append(ObjectList.JsonFactory.from_json(item))
            return obj

