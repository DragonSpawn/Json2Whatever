using SimpleJSON;

/////////////////////////////////////////////////////////////////////////////////////
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/* Date: 2015-01-06                                                                */
/////////////////////////////////////////////////////////////////////////////////////

namespace Generated
{
    public class GlossEntry
    {
        public GlossEntry()
        {
            SortAs = string.Empty;
            GlossTerm = string.Empty;
            Acronym = string.Empty;
            Abbrev = string.Empty;
            GlossSee = string.Empty;
        }

        public int Id {get; set;}
        public float TestFloat {get; set;}
        public string SortAs {get; set;}
        public string GlossTerm {get; set;}
        public string Acronym {get; set;}
        public string Abbrev {get; set;}
        public GlossDef GlossDef {get; set;}
        public string GlossSee {get; set;}

        public static class SimpleJsonFactory
        {
            public static JSONNode ToJson(GlossEntry obj)
            {
                var json = new JSONClass();
                json["id"] = new JSONData(obj.Id);
                json["testFloat"] = new JSONData(obj.TestFloat);
                json["sortAs"] = new JSONData(obj.SortAs);
                json["glossTerm"] = new JSONData(obj.GlossTerm);
                json["acronym"] = new JSONData(obj.Acronym);
                json["abbrev"] = new JSONData(obj.Abbrev);
                json["glossDef"] = obj.GlossDef != null ? Generated.GlossDef.SimpleJsonFactory.ToJson(obj.GlossDef) : null;
                json["glossSee"] = new JSONData(obj.GlossSee);
                return json;
            }

            public static GlossEntry FromJson(JSONNode json)
            {
                var id = json["id"].AsInt;
                var testFloat = json["testFloat"].AsFloat;
                var sortAs = json["sortAs"].Value ?? "";
                var glossTerm = json["glossTerm"].Value ?? "";
                var acronym = json["acronym"].Value ?? "";
                var abbrev = json["abbrev"].Value ?? "";
                var glossDef = json["glossDef"] != null ? Generated.GlossDef.SimpleJsonFactory.FromJson(json["glossDef"]) : null;
                var glossSee = json["glossSee"].Value ?? "";
                return new GlossEntry
                {
                    Id = id,
                    TestFloat = testFloat,
                    SortAs = sortAs,
                    GlossTerm = glossTerm,
                    Acronym = acronym,
                    Abbrev = abbrev,
                    GlossDef = glossDef,
                    GlossSee = glossSee,
                };
            }

        }
    }
}
