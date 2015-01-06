using SimpleJSON;

/////////////////////////////////////////////////////////////////////////////////////
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/* Date: 2015-01-06                                                                */
/////////////////////////////////////////////////////////////////////////////////////

namespace Generated
{
    public class ObjectList
    {
        public ObjectList()
        {
            Name = string.Empty;
        }

        public string Name {get; set;}

        public static class SimpleJsonFactory
        {
            public static JSONNode ToJson(ObjectList obj)
            {
                var json = new JSONClass();
                json["name"] = new JSONData(obj.Name);
                return json;
            }

            public static ObjectList FromJson(JSONNode json)
            {
                var name = json["name"].Value ?? "";
                return new ObjectList
                {
                    Name = name,
                };
            }

        }
    }
}
