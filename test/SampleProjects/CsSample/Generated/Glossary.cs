using SimpleJSON;

/////////////////////////////////////////////////////////////////////////////////////
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/* Date: 2015-01-06                                                                */
/////////////////////////////////////////////////////////////////////////////////////

namespace Generated
{
    public class Glossary
    {
        public Glossary()
        {
            Title = string.Empty;
        }

        public string Title {get; set;}
        public GlossDiv GlossDiv {get; set;}

        public static class SimpleJsonFactory
        {
            public static JSONNode ToJson(Glossary obj)
            {
                var json = new JSONClass();
                json["title"] = new JSONData(obj.Title);
                json["glossDiv"] = obj.GlossDiv != null ? Generated.GlossDiv.SimpleJsonFactory.ToJson(obj.GlossDiv) : null;
                return json;
            }

            public static Glossary FromJson(JSONNode json)
            {
                var title = json["title"].Value ?? "";
                var glossDiv = json["glossDiv"] != null ? Generated.GlossDiv.SimpleJsonFactory.FromJson(json["glossDiv"]) : null;
                return new Glossary
                {
                    Title = title,
                    GlossDiv = glossDiv,
                };
            }

        }
    }
}
