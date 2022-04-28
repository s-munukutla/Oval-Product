import pandas as pd
from temp import *
from modules import *
import re,sys
cert = []
test = []
stater = []
"""Declaring The Sheet Name And Test ID Manually"""

sheet_info = str(input("Enter The Sheet Name:"))
df = pd.read_excel(sys.argv[1], sheet_info)

while True:
   test_id = str(input("Enter the Test Id:"))
   if test_id == '0':
       print("Use Generated Product.xml in the Folder")
       break;
   data = pd.DataFrame(df,columns=['TEST ID','Common Test','Family','Object ID','Object Command'])
   data = data.where(data['TEST ID'] == test_id)
   states_data = pd.DataFrame(df,columns=['State', 'States Regex'])
   family_data = pd.DataFrame(df,columns=['Family'])
   data = data.reset_index()
   states_data = states_data.reset_index()
   data=data.fillna(0)
   states_data = states_data.fillna(0)
   state = {}
   tst = {}
   crt = {}

   '''Grep For The Common Test to Common State'''
   for index, row in data.iterrows():
      if row['Common Test'] != 0:
         Common_Test = row['Common Test'][-5:-1]
         fam=row['Family']
         if fam == "iosxe":
            tst["product"] = "iosxe"
            tst["object_id"] = 2000
         elif fam == "ios":
             tst["product"] = "ios"
             tst["object_id"] = 3000
         elif fam == "asa":
             tst["product"] = "asa"
             tst["object_id"] = 4000
         elif fam == "junos":
             tst["product"] = "junos"
             tst["object_id"] = 7000
         elif fam == "nxos":
             tst["product"] = "nxos"
             tst["object_id"] = 8000
         else:
            print("Object id is Miss Match")
          
         for index_state, states in states_data.iterrows():
            if states['State'] != 0 and Common_Test != 0 :
               states_val = states['State'][-4:]
               if states_val == Common_Test:
                     if fam == "junos":
                         crt["test_id"] = test_id
                         crt["Comment"] = row['Common Test'].split("(")[0]
                         tst["product"] = row['Family']
                         tst["test_id"] = test_id
                         state["product"] = row['Family']
                         state["state_id"] = tst["state_id"] = states['State']
                         tst["Comment"] = row['Common Test'].split("(")[0]
                         state["Comment"] = row['Common Test'].split("(")[0]
                         state["state_regex"] = states['States Regex']
                         cert.append(crt)
                         test.append(tst)
                         stater.append(state)
                     else:
                        crt["test_id"] = test_id
                        crt["Comment"] = row['Common Test'].split("(")[0]
                        tst["product"] = row['Family']
                        tst["test_id"] = test_id
                        tst["state_id"] = states['State']
                        tst["Comment"] = row['Common Test'].split("(")[0]
                        state["product"] = row['Family']
                        state["state_id"] = states['State']
                        state["state_regex"] = states['States Regex']
                        state["Comment"] = row['Common Test'].split("(")[0]
                        cert.append(crt)
                        test.append(tst)
                        stater.append(state)
build_crt(cert)
build_jun_id(test)
build_jun_state(stater)

