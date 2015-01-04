using System.Collections.Generic;
using SimpleJSON;

/////////////////////////////////////////////////////////////////////////////////////
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/* Date: 2015-01-04                                                                */
/////////////////////////////////////////////////////////////////////////////////////

namespace Json2Whatever
{
    public class Person
    {
        public Person()
        {
            Name = string.Empty;
            Country = string.Empty;
            Family = new List<Person>();
        }

        public Person(JSONNode jsonObject)
        {
            Name = jsonObject["name"];
            Age = jsonObject["age"].AsInt;
            Country = jsonObject["country"];
            Family = new List<Person>();
            foreach(JSONNode item in jsonObject["family"].AsArray)
            {
                Family.Add(new Person(item));
            }
        }

        public string Name {get; set;}
        public int Age {get; set;}
        public string Country {get; set;}
        public List<Person> Family {get; set;}

        public JSONNode ToJson()
        {
            var json = new JSONClass();
            json["name"] = new JSONData(Name);
            json["age"] = new JSONData(Age);
            json["country"] = new JSONData(Country);
            foreach(var item in Family)
            {
                json["family"].Add(item.ToJson());
            }
            return json;
        }
    }
}
