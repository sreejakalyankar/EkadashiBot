# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"




# class ActionWhenNextEkadashi(Action):

#     def name(self) -> Text:
#         return "action_when_next_ekadashi"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text = f"Ekadashi Date : rasa.calendar{'ekadashi_date'}")

#         return []
       


#next ekadashi name starts here

import mysql.connector
import pandas as pd
import json
from rasa_sdk import Action
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionNextEkadashiName(Action):

     def name(self):
        return "action_next_ekadashi_name"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="bansilal", 
            database="rasa"
        
    )

        
        ekadashi_name = tracker.get_slot('name')
        query = 'SELECT E.name FROM rasa.ekadashi E JOIN rasa.calendar C ON E.id = C.ekadashi_id WHERE curdate() <= ekadashi_date ORDER BY ekadashi_date LIMIT 1;'

        cursor = mydb.cursor()
        cursor.execute(query, (ekadashi_name))
        name = cursor.fetchall() 
        
        listToStr = ''.join(map(str, name))
        tupleToStr1 = ''.join(map(str,  listToStr ))

        punctuations = "(''),"
        no_punct = ""
        for char in tupleToStr1:
            if char not in punctuations:
                no_punct =  no_punct+char
        msg = 'The next ekadashi name is {}'.format(no_punct)
        dispatcher.utter_message(msg)

#next ekadashi name code ends here

#next ekadashi story code starts here

import mysql.connector
import pandas as pd
import json
from rasa_sdk import Action
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionNextEkadashiStory(Action):

     def name(self):
        return "action_next_ekadashi_story"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="bansilal", 
            database="rasa"
        
    )

        
        ekadashi_story = tracker.get_slot('story')
        query = 'SELECT E.story FROM rasa.ekadashi E JOIN rasa.calendar C ON E.id = C.ekadashi_id WHERE curdate() <= ekadashi_date ORDER BY ekadashi_date LIMIT 1;'

        cursor = mydb.cursor()
        cursor.execute(query, (ekadashi_story))
        name = cursor.fetchall() 
        
        listToStr = ''.join(map(str, name))
        tupleToStr1 = ''.join(map(str,  listToStr ))

        punctuations = "(''),"
        no_punct = ""
        for char in tupleToStr1:
            if char not in punctuations:
                no_punct =  no_punct+char
        msg = 'Here is the link for the next ekadashi story. Please go through. {}'.format(no_punct)
        dispatcher.utter_message(msg)

#next ekadashi story code ends here

#parana timing code starts here

import datetime
import mysql.connector
import pandas as pd
import json
from rasa_sdk import Action
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionParanStartAndEnd(Action):

     def name(self):
        return "action_paran_start_and_end"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="bansilal", 
            database="rasa"
        
    )

        
        paran_start_time = tracker.get_slot('paran_start_time')
        query = 'SELECT CAST(paran_start_time AS char) parana_start_time FROM rasa.calendar WHERE curdate() <= ekadashi_date ORDER BY ekadashi_date LIMIT 1;'
        
        cursor = mydb.cursor()
        cursor.execute(query, (paran_start_time))
        name = cursor.fetchall() 
        
        listToStr = ''.join(map(str, name))
        tupleToStr = ''.join(map(str,  listToStr ))

        punctuations = "(''),"
        no_punct = ""
        for char in tupleToStr:
            if char not in punctuations:
                no_punct =  no_punct+char

        dt = datetime.datetime.strptime(no_punct, '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M')


        paran_end_time = tracker.get_slot('paran_end_time')
        query1 = 'SELECT CAST(paran_end_time AS char) parana_end_time FROM rasa.calendar WHERE curdate() <= ekadashi_date ORDER BY ekadashi_date LIMIT 1;'
        
        cursor1 = mydb.cursor()
        cursor1.execute(query1, (paran_end_time))
        name1 = cursor1.fetchall() 
        
        listToStr1 = ''.join(map(str, name1))
        tupleToStr1 = ''.join(map(str,  listToStr1 ))

        punctuations1 = "(''),"
        no_punct1 = ""
        for char in tupleToStr1:
            if char not in punctuations1:
                no_punct1 =  no_punct1+char
        
        dt1 = datetime.datetime.strptime(no_punct1, '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M')


        msg = 'The parana in New Delhi starts at {} AM and ends at {} AM'.format(dt, dt1)
        dispatcher.utter_message(msg)


#parana timing code ends here


#banglore parana timing code starts here

import mysql.connector
import pandas as pd
import json
from rasa_sdk import Action
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionBangloreParanTiming(Action):

     def name(self):
        return "action_banglore_paran_timing"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="bansilal", 
            database="rasa"
        
    )

        
        banglore_paran_start = tracker.get_slot('banglore_paran_start')
        query = 'SELECT CAST(banglore_paran_start AS char) banglore_parana_start FROM rasa.calendar_location WHERE curdate() <= ekadashi_date ORDER BY ekadashi_date LIMIT 1;'
        
        cursor = mydb.cursor()
        cursor.execute(query, (banglore_paran_start))
        name = cursor.fetchall() 
        
        listToStr = ''.join(map(str, name))
        tupleToStr = ''.join(map(str,  listToStr ))

        punctuations = "(''),"
        no_punct = ""
        for char in tupleToStr:
            if char not in punctuations:
                no_punct =  no_punct+char

        dt = datetime.datetime.strptime(no_punct, '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M')


        banglore_paran_end = tracker.get_slot('banglore_paran_end')
        query1 = 'SELECT CAST(banglore_paran_end AS char) banglore_parana_end FROM rasa.calendar_location WHERE curdate() <= ekadashi_date ORDER BY ekadashi_date LIMIT 1;'
        
        cursor1 = mydb.cursor()
        cursor1.execute(query1, (banglore_paran_end))
        name1 = cursor1.fetchall() 
        
        listToStr1 = ''.join(map(str, name1))
        tupleToStr1 = ''.join(map(str,  listToStr1 ))

        punctuations1 = "(''),"
        no_punct1 = ""
        for char in tupleToStr1:
            if char not in punctuations1:
                no_punct1 =  no_punct1+char

        dt1 = datetime.datetime.strptime(no_punct1, '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M')


        msg = 'The parana in Banglore starts at {} AM and ends at {} AM'.format(dt, dt1)
        dispatcher.utter_message(msg)


#banglore parana timing code ends here

#hyderabad parana timing code starts here

import mysql.connector
import pandas as pd
import json
from rasa_sdk import Action
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHyderabadParanTiming(Action):

     def name(self):
        return "action_hyderabad_paran_timing"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="bansilal", 
            database="rasa"
        
    )

        
        hyderabad_paran_start = tracker.get_slot('hyderabad_paran_start')
        query = 'SELECT CAST(hyderabad_paran_start AS char) hyderabad_parana_start FROM rasa.calendar_location WHERE curdate() <= ekadashi_date ORDER BY ekadashi_date LIMIT 1;'
        
        cursor = mydb.cursor()
        cursor.execute(query, (hyderabad_paran_start))
        name = cursor.fetchall() 
        
        listToStr = ''.join(map(str, name))
        tupleToStr = ''.join(map(str,  listToStr ))

        punctuations = "(''),"
        no_punct = ""
        for char in tupleToStr:
            if char not in punctuations:
                no_punct =  no_punct+char

        dt = datetime.datetime.strptime(no_punct, '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M')


        hyderabad_paran_end = tracker.get_slot('hyderabad_paran_end')
        query1 = 'SELECT CAST(hyderabad_paran_end AS char) hyderabad_parana_end FROM rasa.calendar_location WHERE curdate() <= ekadashi_date ORDER BY ekadashi_date LIMIT 1;'
        
        cursor1 = mydb.cursor()
        cursor1.execute(query1, (hyderabad_paran_end))
        name1 = cursor1.fetchall() 
        
        listToStr1 = ''.join(map(str, name1))
        tupleToStr1 = ''.join(map(str,  listToStr1 ))

        punctuations1 = "(''),"
        no_punct1 = ""
        for char in tupleToStr1:
            if char not in punctuations1:
                no_punct1 =  no_punct1+char

        
        dt1 = datetime.datetime.strptime(no_punct1, '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M')

        msg = 'The parana in Hyderabad starts at {} AM and ends at {} AM'.format(dt, dt1)
        dispatcher.utter_message(msg)


#paran timing code for hyderabad ends here 

#next ekadashi date for Banglore code starts here

import mysql.connector
from rasa_sdk import Action
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionWhenNextEkadashiBang(Action):
     def name(self):
        return "action_when_next_ekadashi_bang"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="bansilal", 
            database="rasa"
        
    )

        
        ekadashi_date = tracker.get_slot('ekadashi_date')
        query = 'SELECT DATE_FORMAT(ekadashi_date, "%d-%m-%Y") FROM rasa.calendar WHERE curdate() <= ekadashi_date ORDER BY ekadashi_date LIMIT 1;'

        cursor = mydb.cursor()
        cursor.execute(query, (ekadashi_date))
        name = cursor.fetchall() 
        
        listToStr = ''.join(map(str, name))
        tupleToStr1 = ''.join(map(str,  listToStr ))

        punctuations = "(''),"
        no_punct = ""
        for char in tupleToStr1:
            if char not in punctuations:
                no_punct =  no_punct+char

           
        msg = 'The next ekadashi in Banglore is on {}'.format(no_punct)
        dispatcher.utter_message(msg)
        
            

#next ekadashi date for Banglore code ends here  

#next ekadashi date for Hyderabad code starts here

import mysql.connector
from rasa_sdk import Action
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionWhenNextEkadashiHyd(Action):
     def name(self):
        return "action_when_next_ekadashi_hyd"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="bansilal", 
            database="rasa"
        
    )

        
        ekadashi_date1 = tracker.get_slot('ekadashi_date')
        query = 'SELECT DATE_FORMAT(ekadashi_date, "%d-%m-%Y") FROM rasa.calendar WHERE curdate() <= ekadashi_date ORDER BY ekadashi_date LIMIT 1;'

        cursor = mydb.cursor()
        cursor.execute(query, (ekadashi_date1))
        name = cursor.fetchall() 
        
        listToStr = ''.join(map(str, name))
        tupleToStr1 = ''.join(map(str,  listToStr ))

        punctuations = "(''),"
        no_punct = ""
        for char in tupleToStr1:
            if char not in punctuations:
                no_punct =  no_punct+char

           
        msg = 'The next ekadashi in Hyderabad is on {}'.format(no_punct)
        dispatcher.utter_message(msg)


#next ekadashi date for Hyderabad ends here

#next ekadashi date for Los Angeles(USA) code starts here

import mysql.connector
from rasa_sdk import Action
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionWhenNextEkadashiUSA(Action):
     def name(self):
        return "action_when_next_ekadashi_usa"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="bansilal", 
            database="rasa"
        
    )

        
        ekd_date_usa  = tracker.get_slot('ekd_date_usa')
        query = 'SELECT DATE_FORMAT(ekd_date_usa, "%d-%m-%Y") FROM rasa.calendar_usa WHERE curdate() <= ekd_date_usa ORDER BY ekd_date_usa LIMIT 1;'

        cursor = mydb.cursor()
        cursor.execute(query, (ekd_date_usa))
        name = cursor.fetchall() 
        
        listToStr = ''.join(map(str, name))
        tupleToStr1 = ''.join(map(str,  listToStr ))

        punctuations = "(''),"
        no_punct = ""
        for char in tupleToStr1:
            if char not in punctuations:
                no_punct =  no_punct+char

           
        msg = 'The next ekadashi in USA is on {}'.format(no_punct)
        dispatcher.utter_message(msg)


#next ekadashi date for Los Angeles(USA) ends here

#next ekadashi date for London(Europe) code starts here

import mysql.connector
from rasa_sdk import Action
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionWhenNextEkadashiEuro(Action):
     def name(self):
        return "action_when_next_ekadashi_euro"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="bansilal", 
            database="rasa"
        
    )

        
        ekd_date_europe  = tracker.get_slot('ekd_date_europe')
        query = 'SELECT DATE_FORMAT(ekd_date_europe, "%d-%m-%Y") FROM rasa.calendar_europe WHERE curdate() <= ekd_date_europe ORDER BY ekd_date_europe LIMIT 1;'

        cursor = mydb.cursor()
        cursor.execute(query, (ekd_date_europe))
        name = cursor.fetchall() 
        
        listToStr = ''.join(map(str, name))
        tupleToStr1 = ''.join(map(str,  listToStr ))

        punctuations = "(''),"
        no_punct = ""
        for char in tupleToStr1:
            if char not in punctuations:
                no_punct =  no_punct+char

           
        msg = 'The next ekadashi in Europe is on {}'.format(no_punct)
        dispatcher.utter_message(msg)


#next ekadashi date for London(Europe) code ends here

#Los Angeles(USA) parana timing code starts here

import mysql.connector
import pandas as pd
import json
from rasa_sdk import Action
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionUsaParanTiming(Action):

     def name(self):
        return "action_usa_paran_timing"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="bansilal", 
            database="rasa"
        
    )

        
        usa_paran_start = tracker.get_slot('usa_paran_start')
        query = 'SELECT CAST(usa_paran_start AS char) usa_parana_start FROM rasa.calendar_usa WHERE curdate() <= ekd_date_usa  ORDER BY ekd_date_usa LIMIT 1;'
        
        cursor = mydb.cursor()
        cursor.execute(query, (usa_paran_start))
        name = cursor.fetchall() 
        
        listToStr = ''.join(map(str, name))
        tupleToStr = ''.join(map(str,  listToStr ))

        punctuations = "(''),"
        no_punct = ""
        for char in tupleToStr:
            if char not in punctuations:
                no_punct =  no_punct+char

        dt = datetime.datetime.strptime(no_punct, '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M')


        usa_paran_end = tracker.get_slot('usa_paran_end')
        query1 = 'SELECT CAST(usa_paran_end AS char) usa_parana_end FROM rasa.calendar_usa WHERE curdate() <= ekd_date_usa  ORDER BY ekd_date_usa LIMIT 1;'
        
        cursor1 = mydb.cursor()
        cursor1.execute(query1, (usa_paran_end))
        name1 = cursor1.fetchall() 
        
        listToStr1 = ''.join(map(str, name1))
        tupleToStr1 = ''.join(map(str,  listToStr1 ))

        punctuations1 = "(''),"
        no_punct1 = ""
        for char in tupleToStr1:
            if char not in punctuations1:
                no_punct1 =  no_punct1+char

        dt1 = datetime.datetime.strptime(no_punct1, '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M')


        msg = 'The parana in USA starts at {} AM and ends at {} AM'.format(dt, dt1)
        dispatcher.utter_message(msg)


#paran timing code for Los Angeles (USA) ends here 


#London (Europe) parana timing code starts here

import mysql.connector
import pandas as pd
import json
from rasa_sdk import Action
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionEuroParanTiming(Action):

     def name(self):
        return "action_euro_paran_timing"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="bansilal", 
            database="rasa"
        
    )

        
        europe_paran_start = tracker.get_slot('europe_paran_start')
        query = 'SELECT CAST(europe_paran_start AS char) europe_parana_start FROM rasa.calendar_europe WHERE curdate() <= ekd_date_europe ORDER BY ekd_date_europe LIMIT 1;'
        
        cursor = mydb.cursor()
        cursor.execute(query, (europe_paran_start))
        name = cursor.fetchall() 
        
        listToStr = ''.join(map(str, name))
        tupleToStr = ''.join(map(str,  listToStr ))

        punctuations = "(''),"
        no_punct = ""
        for char in tupleToStr:
            if char not in punctuations:
                no_punct =  no_punct+char

        dt = datetime.datetime.strptime(no_punct, '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M')


        europe_paran_end = tracker.get_slot('europe_paran_end')
        query1 = 'SELECT CAST(europe_paran_end AS char) europe_parana_end FROM rasa.calendar_europe WHERE curdate() <= ekd_date_europe  ORDER BY ekd_date_europe LIMIT 1;'
        
        cursor1 = mydb.cursor()
        cursor1.execute(query1, (europe_paran_end))
        name1 = cursor1.fetchall() 
        
        listToStr1 = ''.join(map(str, name1))
        tupleToStr1 = ''.join(map(str,  listToStr1 ))

        punctuations1 = "(''),"
        no_punct1 = ""
        for char in tupleToStr1:
            if char not in punctuations1:
                no_punct1 =  no_punct1+char

        dt1 = datetime.datetime.strptime(no_punct1, '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M')


        msg = 'The parana in Europe starts at {} AM and ends at {} AM'.format(dt, dt1)
        dispatcher.utter_message(msg)


#paran timing code for London (Europe) ends here 

#next ekadashi date for New Delhi code starts here

import mysql.connector
from rasa_sdk import Action
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionWhenNextEkadashiDelhi(Action):
     def name(self):
        return "action_when_next_ekadashi_delhi"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="bansilal", 
            database="rasa"
        
    )

        
        ekadashi_date2 = tracker.get_slot('ekadashi_date')
        query = 'SELECT DATE_FORMAT(ekadashi_date, "%d-%m-%Y") FROM rasa.calendar WHERE curdate() <= ekadashi_date ORDER BY ekadashi_date LIMIT 1;'

        cursor = mydb.cursor()
        cursor.execute(query, (ekadashi_date2))
        name = cursor.fetchall() 
        
        listToStr = ''.join(map(str, name))
        tupleToStr1 = ''.join(map(str,  listToStr ))

        punctuations = "(''),"
        no_punct = ""
        for char in tupleToStr1:
            if char not in punctuations:
                no_punct =  no_punct+char
  
        msg = 'The next ekadashi in New Delhi is on {}'.format(no_punct)
        dispatcher.utter_message(msg)
        
            

#next ekadashi date for New Delhi code ends here 

#ekadashi dates list for india code starts here

import mysql.connector
from rasa_sdk import Action
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionEkadashiDateListIndia(Action):
     def name(self):
        return "action_ekadashi_date_list_india"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="bansilal", 
            database="rasa"
        
    )

        
        ekadashi_date_list = tracker.get_slot('ekadashi_date')
        query = 'SELECT DATE_FORMAT(ekadashi_date, "%d-%m-%Y") FROM rasa.calendar WHERE curdate() <= ekadashi_date ORDER BY ekadashi_date LIMIT 2;'

        cursor = mydb.cursor()
        cursor.execute(query, (ekadashi_date_list))
        name = cursor.fetchall() 
        
        listToStr = ''.join(map(str, name))
        tupleToStr1 = ''.join(map(str,  listToStr ))

        punctuations = "('')"
        no_punct = ""
        for char in tupleToStr1:
            if char not in punctuations:
                no_punct =  no_punct+char
  
        msg = 'The list of ekadashi dates are {} for next month.'.format(no_punct)
        dispatcher.utter_message(msg)

#ekadashi dates list for india code ends here

#ekadashi dates list for europe code starts here

import mysql.connector
from rasa_sdk import Action
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionEkadashiDateListEuro(Action):
     def name(self):
        return "action_ekadashi_date_list_euro"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="bansilal", 
            database="rasa"
        
    )

        
        ekd_date_europe_list = tracker.get_slot('ekd_date_europe')
        query = 'SELECT DATE_FORMAT(ekd_date_europe, "%d-%m-%Y") FROM rasa.calendar_europe WHERE curdate() <= ekd_date_europe ORDER BY ekd_date_europe LIMIT 2;'

        cursor = mydb.cursor()
        cursor.execute(query, (ekd_date_europe_list))
        name = cursor.fetchall() 
        
        listToStr = ''.join(map(str, name))
        tupleToStr1 = ''.join(map(str,  listToStr ))

        punctuations = "('')"
        no_punct = ""
        for char in tupleToStr1:
            if char not in punctuations:
                no_punct =  no_punct+char
  
        msg = 'The next month ekadashi dates are {} for Europe Location.'.format(no_punct)
        dispatcher.utter_message(msg)

#ekadashi dates list for europe code ends here

#ekadashi dates list for usa code starts here

import mysql.connector
from rasa_sdk import Action
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionEkadashiDateListUsa(Action):
     def name(self):
        return "action_ekadashi_date_list_usa"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="bansilal", 
            database="rasa"
        
    )

        
        ekd_date_usa_list = tracker.get_slot('ekd_date_usa')
        query = 'SELECT DATE_FORMAT(ekd_date_usa, "%d-%m-%Y") FROM rasa.calendar_usa WHERE curdate() <= ekd_date_usa ORDER BY ekd_date_usa LIMIT 2;'

        cursor = mydb.cursor()
        cursor.execute(query, (ekd_date_usa_list))
        name = cursor.fetchall() 
        
        listToStr = ''.join(map(str, name))
        tupleToStr1 = ''.join(map(str,  listToStr ))

        punctuations = "('')"
        no_punct = ""
        for char in tupleToStr1:
            if char not in punctuations:
                no_punct =  no_punct+char
  
        msg = 'The next month ekadashi dates are {} for USA Location.'.format(no_punct)
        dispatcher.utter_message(msg)

#ekadashi dates list for europe code ends here

#previous ekadashi name code starts here

import mysql.connector
import pandas as pd
import json
from rasa_sdk import Action
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionPreviousEkadashiName(Action):

     def name(self):
        return "action_previous_ekadashi_name"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="bansilal", 
            database="rasa"
        
    )

        
        ekadashi_prev_name = tracker.get_slot('name')
        query = 'SELECT E.name FROM rasa.ekadashi E JOIN rasa.calendar C ON E.id = C.ekadashi_id WHERE ekadashi_date <= curdate() ORDER BY ekadashi_date desc LIMIT 1;'

        cursor = mydb.cursor()
        cursor.execute(query, (ekadashi_prev_name))
        name = cursor.fetchall() 
        
        listToStr = ''.join(map(str, name))
        tupleToStr1 = ''.join(map(str,  listToStr ))

        punctuations = "(''),"
        no_punct = ""
        for char in tupleToStr1:
            if char not in punctuations:
                no_punct =  no_punct+char

        msg = 'The previous ekadashi name was {}'.format(no_punct)
        dispatcher.utter_message(msg)

#previous ekadashi name code ends here

#how many days for ekadashi in India code starts here

import mysql.connector
import pandas as pd
import json
from rasa_sdk import Action
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionDaysLeftIndia(Action):

     def name(self):
        return "action_days_left_india"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="bansilal", 
            database="rasa"
        
    )

        
        days_left_india = tracker.get_slot('ekadashi_date')
        query = 'SELECT DATEDIFF(ekadashi_date, CURDATE()) FROM rasa.calendar WHERE ekadashi_date > curdate() ORDER BY ekadashi_date LIMIT 1;'

        cursor = mydb.cursor()
        cursor.execute(query, (days_left_india))
        name = cursor.fetchall() 
        
        listToStr = ''.join(map(str, name))
        tupleToStr1 = ''.join(map(str,  listToStr ))

        punctuations = "(''),"
        no_punct = ""
        for char in tupleToStr1:
            if char not in punctuations:
                no_punct =  no_punct+char

        msg = 'The number of days left out for next ekadashi is {}'.format(no_punct)
        dispatcher.utter_message(msg)

#how many days for ekadashi code in India ends here

#how many days for ekadashi in Europe code starts here

import mysql.connector
import pandas as pd
import json
from rasa_sdk import Action
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionDaysLeftEuro(Action):

     def name(self):
        return "action_days_left_euro"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="bansilal", 
            database="rasa"
        
    )

        
        days_left_euro = tracker.get_slot('ekd_date_europe')
        query = 'SELECT DATEDIFF(ekd_date_europe, CURDATE()) FROM rasa.calendar_europe WHERE ekd_date_europe > curdate() ORDER BY ekd_date_europe LIMIT 1;'

        cursor = mydb.cursor()
        cursor.execute(query, (days_left_euro))
        name = cursor.fetchall() 
        
        listToStr = ''.join(map(str, name))
        tupleToStr1 = ''.join(map(str,  listToStr ))

        punctuations = "(''),"
        no_punct = ""
        for char in tupleToStr1:
            if char not in punctuations:
                no_punct =  no_punct+char

        msg = 'The number of days left out for next ekadashi in Europe is {}'.format(no_punct)
        dispatcher.utter_message(msg)

#how many days for ekadashi code in Europe ends here

#how many days for ekadashi in USA code starts here

import mysql.connector
import pandas as pd
import json
from rasa_sdk import Action
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionDaysLeftUsa(Action):

     def name(self):
        return "action_days_left_usa"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="bansilal", 
            database="rasa"
        
    )

        
        days_left_usa = tracker.get_slot('ekd_date_usa')
        query = 'SELECT DATEDIFF(ekd_date_usa, CURDATE()) FROM rasa.calendar_usa WHERE ekd_date_usa > curdate() ORDER BY ekd_date_usa LIMIT 1;'

        cursor = mydb.cursor()
        cursor.execute(query, (days_left_usa))
        name = cursor.fetchall() 
        
        listToStr = ''.join(map(str, name))
        tupleToStr1 = ''.join(map(str,  listToStr ))

        punctuations = "(''),"
        no_punct = ""
        for char in tupleToStr1:
            if char not in punctuations:
                no_punct =  no_punct+char

        msg = 'The number of days left out for next ekadashi in USA is {}'.format(no_punct)
        dispatcher.utter_message(msg)

#how many days for ekadashi code in USA ends here

