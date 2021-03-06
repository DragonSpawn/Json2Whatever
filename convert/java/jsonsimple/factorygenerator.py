from convert.base.factorygenerator import BaseFactoryGenerator
from convert.base.parsedobject import ParsedObjectType


class FactoryGenerator(BaseFactoryGenerator):
    def generate_import(self):
        result = ("import org.json.simple.JSONObject;\n"
                  "import org.json.simple.JSONValue;\n"
                  "import java.util.List;\n"
                  "import java.util.ArrayList;\n"
                  "import org.json.simple.JSONArray;\n")
        return result

    def _generate_from_json(self):
        constructor = ("        public static {0} fromJson(String jsonString) {{\n"
                       "            JSONObject jsonObject = (JSONObject)JSONValue.parse(jsonString);\n"
                       "            return fromJsonObject(jsonObject);\n"
                       "        }}\n"
                       "\n"
                       "        public static List<{0}> fromJsonArray(String jsonArrayString) {{\n"
                       "            JSONArray jsonArray = (JSONArray)JSONValue.parse(jsonArrayString);\n"
                       "            List<{0}> result = new ArrayList<{0}>();\n"
                       "            for(Object jsonObject : jsonArray)\n"
                       "            {{\n"
                       "                result.add(fromJsonObject((JSONObject)jsonObject));\n"
                       "            }}\n"
                       "            return result;\n"
                       "        }}\n\n"
                       "        public static {0} fromJsonObject(JSONObject jsonObject) {{\n"
                       "            if(jsonObject == null) {{\n"
                       "                return null;\n"
                       "            }}\n"
                       "            {0} obj = new {0}();\n").format(_capitalize(self.data.type_name))

        # member initialization
        for member in self.data.data:
            constructor += _member_initialization(member)

        constructor += ("            return obj;\n"
                        "        }\n")
        return constructor

    def _generate_to_json(self):
        serializer = ("        public static String toJson({0} obj) {{\n"
                      "            JSONObject json = toJsonObject(obj);\n"
                      "            return json.toString();\n"
                      "        }}\n\n"
                      "        public static String toJson(List<{0}> list) {{\n"
                      "            JSONArray array = new JSONArray();\n"
                      "            for({0} obj : list)\n"
                      "            {{\n"
                      "                array.add(toJsonObject(obj));\n"
                      "            }}\n"
                      "            return array.toString();\n"
                      "        }}\n"
                      "\n"
                      "        public static JSONObject toJsonObject({0} obj) {{\n"
                      "            JSONObject json = new JSONObject();\n").format(_capitalize(self.data.type_name))

        for member in self.data.data:
            if member.type == ParsedObjectType.Array:
                serializer += "            JSONArray tempArray;\n"
                break

        for member in self.data.data:
            if member.type == ParsedObjectType.Object:
                serializer += _serialize_object_member(member)
            elif member.type == ParsedObjectType.Array:
                serializer += _serialize_array_member(member)
            else:
                accessor_str = ""
                if member.type == ParsedObjectType.Enum:
                    accessor_str = ".getValue()"
                serializer += "            json.put(\"{0}\", obj.{1}{2});\n".format(member.name, member.name, accessor_str)

        serializer += ("            return json;\n"
                       "        }\n")

        return serializer

    def generate(self, data, namespace):
        self.data = data
        self.namespace = namespace
        serializers = ("\n    public static class JsonSimpleFactory\n"
                       "    {\n")
        serializers += self._generate_to_json()
        serializers += self._generate_from_json()
        serializers += "    }\n"
        return serializers


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


def _member_initialization(member):
    """
    Generated the code for initialization of the members in the constructor.
    :type member: ParsedMember
    :param member:
    :return:
    """
    json_container_string = "jsonObject.get(\"{0}\")".format(member.name)

    if member.type == ParsedObjectType.Object:
        return "            obj.{0} = !jsonObject.containsKey(\"{0}\") ? null : {1};\n".format(member.name, _get_member_initialization_string(member, json_container_string))
    elif member.type == ParsedObjectType.Enum:
        return ("            if(jsonObject.containsKey(\"{0}\")) {{\n"
                "                obj.{0} = new {2}((Long){1});\n"
                "            }}\n").format(member.name, _get_member_initialization_string(member, json_container_string), _get_type_name(member, False))
    elif member.type == ParsedObjectType.Array:
        result = ("            if(jsonObject.containsKey(\"{0}\")) {{\n"
                  "                obj.{0} = new ArrayList<{1}>();\n"
                  "                for(Object item : (JSONArray)jsonObject.get(\"{2}\")) {{\n").format(member.name, _get_type_name(member.data[0], False), member.name)
        child = member.data[0]

        if child.type == ParsedObjectType.Object:
            result += "                    obj.{0}.add({1}.JsonSimpleFactory.fromJsonObject((JSONObject)item));\n".format(member.name, _capitalize(child.type_name))
        else:
            result += "                    obj.{0}.add(({1})item);\n".format(member.name, _get_type_name(child, False))
        result += ("                }\n"
                   "            }\n")
        return result
    else:
        return ("            if(jsonObject.containsKey(\"{0}\")) {{\n"
                "                obj.{0} = ({2}){1};\n"
                "            }}\n").format(member.name, _get_member_initialization_string(member, json_container_string), _get_type_name(member, False))


def _get_member_initialization_string(member, json_container):
    if member.type == ParsedObjectType.Object:
        return "{0}.JsonSimpleFactory.fromJsonObject((JSONObject){1})".format(_capitalize(member.type_name), json_container)
    if member.type == ParsedObjectType.Array:
        return "new {0}".format(_get_type_name(member))
    return "{0}{1}".format(json_container, "")


def _get_type_name(member, primitive=True):
    """
    If a ParsedClass is supplied then it returns the object name with a captialized first letter (myClass => MyClass)
    For ParsedMember it returns the type of the member (myString => string)
    :type member: ParsedMember
    :param obj:
    :return:
    """
    if member.type == ParsedObjectType.String:
        return "String"
    if member.type == ParsedObjectType.Int or member.type == ParsedObjectType.Float or member.type == ParsedObjectType.Bool:
        if not primitive:
            if member.type == ParsedObjectType.Int:
                return "Long"
            elif member.type == ParsedObjectType.Bool:
                return "Boolean"
            else:
                return "Float"
        return member.type.name.lower()
    if member.type == ParsedObjectType.Array:
        return "List<{0}>".format(_get_type_name(member.data[0], False))
    return _capitalize(member.type_name)


def _serialize_object_member(member):
    return "            json.put(\"{0}\", obj.{0} == null ? null : {1}.JsonSimpleFactory.toJsonObject(obj.{0}));\n".format(member.name, _capitalize(member.type_name))


def _serialize_array_member(member):
    serializer = ("\n            if(obj.{0} != null) {{\n"
                  "                tempArray = new JSONArray();\n"
                  "                for({1} item : obj.{0}){{\n").format(member.name, _get_type_name(member.data[0], False))
    if member.data[0].type == ParsedObjectType.Object:
        serializer += "                    tempArray.add({0}.JsonSimpleFactory.toJsonObject(item));\n".format(_capitalize(member.data[0].type_name))
    else:
        serializer += "                    tempArray.add(item);\n"
    serializer += "                }\n"
    serializer += "                json.put(\"{0}\", tempArray);\n".format(member.name)
    serializer += "            }\n"
    return serializer