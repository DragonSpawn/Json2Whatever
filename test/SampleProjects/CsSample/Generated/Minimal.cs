using SimpleJSON;

/////////////////////////////////////////////////////////////////////////////////////
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/*                                                                                 */
/////////////////////////////////////////////////////////////////////////////////////

namespace Generated
{
    public class Minimal
    {
        public Minimal()
        {
        }


        public static class SimpleJsonFactory
        {
            public static string ToJson(Minimal obj)
            {
                var jsonObject = ToJsonObject(obj);
                return jsonObject.ToString();
            }

            public static JSONNode ToJsonObject(Minimal obj)
            {
                var jsonObject = new JSONClass();
                return jsonObject;
            }

            public static Minimal FromJson(string jsonString)
            {
                var jsonObject = JSON.Parse(jsonString);
                return FromJsonObject(jsonObject);
            }

            public static Minimal FromJsonObject(JSONNode jsonObject)
            {
                return new Minimal
                {
                };
            }

        }
    }
}
