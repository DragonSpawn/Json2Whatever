package Generated;

import org.json.simple.JSONObject;
import org.json.simple.JSONValue;
import java.util.List;
import java.util.ArrayList;
import org.json.simple.JSONArray;
/***********************************************************************************/
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/*                                                                                 */
/***********************************************************************************/

public class Person{
    public Person() {
        name = "";
        country = "";
        gender = new Gender(0);
        family = new ArrayList<Person>();
    }
    public String name;
    public Long age;
    public String country;
    public Boolean isHuman;
    public Glossary myGlossary;
    public Gender gender;
    public List<Person> family;

    public static class JsonSimpleFactory
    {
        public static String toJson(Person obj) {
            JSONObject json = toJsonObject(obj);
            return json.toString();
        }

        public static String toJson(List<Person> list) {
            JSONArray array = new JSONArray();
            for(Person obj : list)
            {
                array.add(toJsonObject(obj));
            }
            return array.toString();
        }

        public static JSONObject toJsonObject(Person obj) {
            JSONObject json = new JSONObject();
            JSONArray tempArray;
            json.put("name", obj.name);
            json.put("age", obj.age);
            json.put("country", obj.country);
            json.put("isHuman", obj.isHuman);
            json.put("myGlossary", obj.myGlossary == null ? null : Glossary.JsonSimpleFactory.toJsonObject(obj.myGlossary));
            json.put("gender", obj.gender.getValue());

            if(obj.family != null) {
                tempArray = new JSONArray();
                for(Person item : obj.family){
                    tempArray.add(Person.JsonSimpleFactory.toJsonObject(item));
                }
                json.put("family", tempArray);
            }
            return json;
        }
        public static Person fromJson(String jsonString) {
            JSONObject jsonObject = (JSONObject)JSONValue.parse(jsonString);
            return fromJsonObject(jsonObject);
        }

        public static List<Person> fromJsonArray(String jsonArrayString) {
            JSONArray jsonArray = (JSONArray)JSONValue.parse(jsonArrayString);
            List<Person> result = new ArrayList<Person>();
            for(Object jsonObject : jsonArray)
            {
                result.add(fromJsonObject((JSONObject)jsonObject));
            }
            return result;
        }

        public static Person fromJsonObject(JSONObject jsonObject) {
            if(jsonObject == null) {
                return null;
            }
            Person obj = new Person();
            if(jsonObject.containsKey("name")) {
                obj.name = (String)jsonObject.get("name");
            }
            if(jsonObject.containsKey("age")) {
                obj.age = (Long)jsonObject.get("age");
            }
            if(jsonObject.containsKey("country")) {
                obj.country = (String)jsonObject.get("country");
            }
            if(jsonObject.containsKey("isHuman")) {
                obj.isHuman = (Boolean)jsonObject.get("isHuman");
            }
            obj.myGlossary = !jsonObject.containsKey("myGlossary") ? null : Glossary.JsonSimpleFactory.fromJsonObject((JSONObject)jsonObject.get("myGlossary"));
            if(jsonObject.containsKey("gender")) {
                obj.gender = new Gender((Long)jsonObject.get("gender"));
            }
            if(jsonObject.containsKey("family")) {
                obj.family = new ArrayList<Person>();
                for(Object item : (JSONArray)jsonObject.get("family")) {
                    obj.family.add(Person.JsonSimpleFactory.fromJsonObject((JSONObject)item));
                }
            }
            return obj;
        }
    }
}
