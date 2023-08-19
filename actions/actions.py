# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import mysql.connector
    
class ActionExtractValue(Action):

    def name(self) -> Text:
        return "action_extract_value"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #value = next(tracker.get_latest_entity_values("value"), None)
        # Connect to the MySQL database
        conn = mysql.connector.connect(
                    host="procurelineserver.mysql.database.azure.com",
                    user="sadmin@procurelineserver",
                    password="Suite@1518",
                    database="pts_career_demo"
        )
        cursor = conn.cursor()
        value = tracker.get_slot("value")
        # Query the database to get data from two tables (e.g., table1 and table2)
        user_message = tracker.latest_message.get("text")
        
        #initial_data = "Hello, how can I assist you today?"
        
        # Replace `column1`, `column2`, etc., with the actual column names you want to fetch from each table
        
        cursor.execute("SELECT A.jid as jobId, A.title, A.job_code, A.city as jobCity, A.state as jobState, A.country as jobCountry, B.first, B.last, B.city as applicantCity, B.country as applicantCountry FROM job_post A JOIN job_apply B ON A.jid = B.job_id WHERE B.applyid = %s",(value,))
        result_table1 = cursor.fetchall()
        for row in result_table1:
            jobid = row[0]
            jobid = row[0]
            title = row[1]
            jobcode = row[2]
            city = row[3]
            state = row[4]
            country = row[5]
            firstname = row[6]
            lastname = row[7]
        

        # Close the database connection
        conn.close()
        dispatcher.utter_message(text=f"Dear {firstname} , I see that you applied for {title}")
        return [SlotSet("value", value),SlotSet("table1_data",result_table1)]
    
    
class ActionExtractPayloadValues(Action):
    def name(self) -> str:
        return "action_extract_payload_values"

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        # Do whatever you want with the data (e.g., formulating a response)
        #response = f"Data from table1: {table1_data}"

        # Send the response to the user
        #dispatcher.utter_message(text=response)
        
        # Get the latest user message
        latest_message = tracker.latest_message

        # Get the entities extracted from the latest message
        entities = latest_message.get("entities", [])

        # Extract payload values if available and set them as slots
        payload_values = {}
        for entity in entities:
            if entity["entity"] == "pythondeveloper":
                payload_values["pythondeveloper"] = entity["value"]
            elif entity["entity"] == "workingshift":
                payload_values["workingshift"] = entity["value"]
            elif entity["entity"] == "currentsalary":
                payload_values["currentsalary"] = entity["value"]
            elif entity["entity"] == "expectedsalary":
                payload_values["expectedsalary"] = entity["value"]
            elif entity["entity"] == "willingtojoin":
                payload_values["willingtojoin"] = entity["value"]
            elif entity["entity"] == "systemavailability":
                payload_values["systemavailability"] = entity["value"]
            elif entity["entity"] == "jobchange":
                payload_values["jobchange"] = entity["value"]
            elif entity["entity"] == "willingtorelocate":
                payload_values["willingtorelocate"] = entity["value"]
            elif entity["entity"] == "offersinhand":
                payload_values["offersinhand"] = entity["value"]
            elif entity["entity"] == "relevantyears":
                payload_values["relevantyears"] = entity["value"]
            elif entity["entity"] == "shortlisted":
                payload_values["shortlisted"] = entity["value"]
                 
            
    
    

        # Set the extracted payload values as slots
        return [SlotSet(key, value) for key, value in payload_values.items()]




class ActionInsertIntoDatabase(Action):
    def name(self) -> str:
        return "action_insert_into_database"

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get the payload values from the slots
        parameter1_value = tracker.get_slot("pythondeveloper")
        parameter2_value = tracker.get_slot("workingshift")
        parameter3_value = tracker.get_slot("currentsalary")
        parameter4_value = tracker.get_slot("expectedsalary")
        parameter5_value = tracker.get_slot("willingtojoin")
        parameter6_value = tracker.get_slot("systemavailability")
        parameter7_value = tracker.get_slot("jobchange")
        parameter8_value = tracker.get_slot("willingtorelocate")
        parameter9_value = tracker.get_slot("offersinhand")
        parameter10_value = tracker.get_slot("relevantyears")
        parameter11_value = tracker.get_slot("shortlisted")
        
        

        # Connect to the MySQL database
        conn = mysql.connector.connect(
                    host="procurelineserver.mysql.database.azure.com",
                    user="sadmin@procurelineserver",
                    password="Suite@1518",
                    database="pts_career_demo"
        )
        cursor = conn.cursor()
        

        # Construct the SQL query
        sql_query = "INSERT INTO pts_smart_agent (Position_applied, Working_Shift,Current_Salary,Expected_Salary,Joining_Time,System_Availability) VALUES (%s,%s,%s,%s,%s,%s)"

        # Execute the query with the payload values
        cursor.execute(sql_query, (parameter1_value, parameter2_value,parameter3_value, parameter4_value,parameter5_value,parameter6_value))
        conn.commit()

        # Close the database connection
        cursor.close()
        conn.close()

        return []


