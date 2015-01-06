using System.Collections.Generic;
using SimpleJSON;

/////////////////////////////////////////////////////////////////////////////////////
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/* Date: 2015-01-06                                                                */
/////////////////////////////////////////////////////////////////////////////////////

namespace Generated
{
    public class GlossDef
    {
        public GlossDef()
        {
            Para = string.Empty;
            GlossSeeAlso = new List<string>();
        }

        public string Para {get; set;}
        public List<string> GlossSeeAlso {get; set;}

        public static class SimpleJsonFactory
        {
            public static JSONNode ToJson(GlossDef obj)
            {
                var json = new JSONClass();
                json["para"] = new JSONData(obj.Para);
                var glossSeeAlso = new JSONArray();
                foreach(var item in obj.GlossSeeAlso)
                {
                    glossSeeAlso.Add(new JSONData(item));
                }
                json["glossSeeAlso"] = glossSeeAlso;

                return json;
            }

            public static GlossDef FromJson(JSONNode json)
            {
                var para = json["para"].Value ?? "";
                var glossSeeAlso = new List<string>();
                foreach(JSONNode item in json["glossSeeAlso"].AsArray)
                {
                    glossSeeAlso.Add(item);
                }

                return new GlossDef
                {
                    Para = para,
                    GlossSeeAlso = glossSeeAlso,
                };
            }

        }
    }
}
