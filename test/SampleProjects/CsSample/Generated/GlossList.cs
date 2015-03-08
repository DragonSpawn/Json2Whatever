using SimpleJSON;

/////////////////////////////////////////////////////////////////////////////////////
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/*                                                                                 */
/////////////////////////////////////////////////////////////////////////////////////

namespace Generated
{
    public class GlossList
    {
        public GlossList()
        {
        }

        public GlossEntry GlossEntry {get; set;}

        public static class SimpleJsonFactory
        {
            public static string ToJson(GlossList obj)
            {
                var jsonObject = ToJsonObject(obj);
                return jsonObject.ToString();
            }

            public static JSONNode ToJsonObject(GlossList obj)
            {
                var jsonObject = new JSONClass();
                if (obj.GlossEntry != null)
                    jsonObject["glossEntry"] = Generated.GlossEntry.SimpleJsonFactory.ToJsonObject(obj.GlossEntry);
                return jsonObject;
            }

            public static GlossList FromJson(string jsonString)
            {
                var jsonObject = JSON.Parse(jsonString);
                return FromJsonObject(jsonObject);
            }

            public static GlossList FromJsonObject(JSONNode jsonObject)
            {
                var glossEntry = jsonObject["glossEntry"] != null ? Generated.GlossEntry.SimpleJsonFactory.FromJsonObject(jsonObject["glossEntry"]) : null;
                return new GlossList
                {
                    GlossEntry = glossEntry,
                };
            }

        }
    }
}
