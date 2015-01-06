import re
from convert.base.generator import BaseGenerator
from convert.base.parsedobject import *
import datetime


class Generator(BaseGenerator):
    def _generate_default_constructor(self):
        constructor = "    def __init__(self):\n"

        if self.data.data.__len__() == 0:
            constructor += "        pass\n"
        else:
            for member in self.data.data:
                if member.type == ParsedObjectType.Array:
                    constructor += "        self._{0} = []\n".format(_camel_case(member.name))
                elif member.type == ParsedObjectType.String:
                    constructor += "        self._{0} = \"\"\n".format(_camel_case(member.name))
                elif member.type == ParsedObjectType.Int:
                    constructor += "        self._{0} = 0\n".format(_camel_case(member.name))
                elif member.type == ParsedObjectType.Float:
                    constructor += "        self._{0} = 0.0\n".format(_camel_case(member.name))
                elif member.type == ParsedObjectType.Object:
                    constructor += "        self._{0} = None\n".format(_camel_case(member.name))
        constructor += "\n"

        return constructor

    def _generate_footer(self):
        return ""

    def _generate_member_access(self):
        result = ""
        for member in self.data.data:
            result += _generate_getter_setter(member)
        result += "\n"
        return result

    def _generate_json_constructor(self):
        constructor = ("    @classmethod\n"
                       "    def load(cls, json_obj):\n"
                       "        \"\"\":type json_obj: dict\n"
                       "           :rtype: {0}\"\"\"\n"
                       "        obj = {0}()\n").format(_capitalize(self.data.name))

        for member in self.data.data:
            constructor += _member_load(member)

        constructor += "        return obj\n\n"

        return constructor

    def _generate_factory(self):
        result = ("    def to_json(self):\n"
                  "        \"\"\":rtype: str\"\"\"\n"
                  "        return {0}.JsonEncoder().encode(self)\n\n"
                  "    class JsonEncoder(json.JSONEncoder):\n"
                  "        def default(self, obj):\n"
                  "            d = {{\n").format(_capitalize(self.data.name))
        for member in self.data.data:
            result += _member_save(member)
        result += "            }\n"
        for member in self.data.data:
            if member.type == ParsedObjectType.Array:
                result += _member_save_list(member)
        result += "            return d"
        return result

    def _generate_header(self):
        result = "import json\n"
        for member in self.data.data:
            if _capitalize(member.name) == _capitalize(self.data.name):
                # if the member is the same class as the current class then we shouldn't import it
                continue
            if member.type == ParsedObjectType.Object:
                result += "from {0} import {1}\n".format(member.name.lower(), _capitalize(member.name))
            elif member.type == ParsedObjectType.Array:
                child = member.data[0]
                if _capitalize(child.name) == _capitalize(self.data.name):
                    continue
                if child.type == ParsedObjectType.Object:
                    result += "from {0} import {1}\n".format(child.name.lower(), _capitalize(child.name))

        date_str = "Date: {0}".format(datetime.date.today())
        date_str = date_str.ljust(82)
        result += ("#####################################################################################\n"
                   "# This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)  #\n"
                   "# Modifications to this file will be lost the next time you run the tool.           #\n"
                   "# {0}#\n"
                   "#####################################################################################\n\n").format(date_str)
        result += "\nclass {0}:\n".format(_capitalize(self.data.name))
        return result

    def file_name(self, json_name):
        return json_name.lower() + ".py"


def _member_save(member):

    if member.type == ParsedObjectType.Object:
        return "            '{0}': obj.{1}.to_json(),\n".format(member.name, _camel_case(member.name))
    if member.type == ParsedObjectType.Array:
        return "                '{0}': [],\n".format(member.name)
    return "                '{0}': obj.{1},\n".format(member.name, _camel_case(member.name))


def _member_save_list(member):
    result = "            for item in obj.{1}:\n".format(member.name, _camel_case(member.name))

    child = member.data[0]
    if child.type == ParsedObjectType.Object:
        result += "                d['family'].append(item.to_json())\n"
    else:
        result += "                d['family'].append(item)\n"
    result += "\n"
    return result


def _member_load(member):
    json_container_string = "json_obj[\"{0}\"]".format(member.name)
    if member.type == ParsedObjectType.Object:
        return "        obj._{0} = {1}({2})\n".format(_camel_case(member.name), _capitalize(member.name), json_container_string)
    elif member.type == ParsedObjectType.Array:
        result = ("        obj._{0} = []\n"
                  "        for item in {1}:\n").format(_camel_case(member.name), json_container_string)
        child = member.data[0]

        if child.type == ParsedObjectType.Object:
            result += "            obj._{0}.append({1}.load(item))\n".format(_camel_case(member.name), _capitalize(child.name))
        else:
            result += "            obj._{0}.append(item)\n".format(_camel_case(member.name))
        return result
    else:
        return "        obj._{0} = {1}\n".format(_camel_case(member.name), json_container_string)


def _camel_case(obj):
    a = re.compile('((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))')
    return a.sub(r'_\1', obj).lower()


def _capitalize(obj):
    """
    Returns the object name with the first letter capitalized (all other untouched).
    :param obj:
    :return:
    """
    if obj.__len__() < 2:
        return obj
    if obj == "string" or obj == "float" or obj == "int":
        return obj
    return obj[0].upper() + obj[1:]


def _generate_getter_setter(member):
    result = ("    @property\n"
              "    def {0}(self):\n"
              "        \"\"\":rtype: {1}\"\"\"\n"
              "        return self._{0}\n"
              "    @{0}.setter\n"
              "    def {0}(self, value):\n"
              "        \"\"\":type value: {1}\n"
              "           :rtype: None\"\"\"\n"
              "        self._{0} = value\n\n").format(_camel_case(member.name), _get_type_name(member))
    return result

def _get_type_name(obj):
    if obj.type == ParsedObjectType.String:
        return "str"
    if obj.type == ParsedObjectType.Object:
        return _capitalize(obj.name)
    if obj.type == ParsedObjectType.Array:
        return "list of [{0}]".format(_get_type_name(obj.data[0]))
    return obj.type.name.lower()