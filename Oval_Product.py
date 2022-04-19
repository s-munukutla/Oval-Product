import pandas as pd
from temp import *
"""Declaring The Sheet Name And Test ID Manually"""

sheet_info = str(input("Enter  The Sheet Name:"))
file = open('Product.xml', 'w')
df = pd.read_excel('/home/surya/Documents/Python/OVAL_Product/Definition ID Database.xlsx', sheet_info)

def build_id(h):
    test_out = tst_id.format(data=h)
    file.writelines(test_out)
    file.write("\n")

def build_state(g):
    state_out= state_id.format(data=g)
    file.writelines(state_out)
    file.write("\n")

while True:
   test_id = str(input("Enter the Test Id:"))
   if test_id == '0':
          break;
   data = pd.DataFrame(df,columns=['TEST ID','Common Test','Family','Object ID','Object Command'])
   data = data.where(data['TEST ID'] == test_id)
   states_data = pd.DataFrame(df,columns=['State', 'States Regex'])
   family_data=pd.DataFrame(df,columns=['Family'])
   data = data.reset_index()
   states_data=states_data.reset_index()
   family_data = family_data.reset_index()
   data=data.fillna(0)
   states_data=states_data.fillna(0)
   state = {}
   tst = {}
   '''Grep For The Common Test to Common State'''
   for index, row in data.iterrows():
      if row['Common Test'] != 0:
         Common_Test = row['Common Test'][-5:-1]
         fam=row['Family']
         if fam == "iosxe":
            tst['product'] = "iosxe"
         elif fam == "ios":
             tst['product'] = "ios"
         elif fam == "asa":
              tst['product'] = "asa"
         elif fam == "junos":
              tst['product'] = "junos"
         elif fam == "nxos":
              tst['product'] = "nxos"
         else:
            print("Object id is Miss Match")
           
         for index_state, states in states_data.iterrows():
            if states['State'] != 0 and Common_Test != 0 :
               states_val = states['State'][-4:]
               if states_val == Common_Test:
                  '''test_id,Comment,state_id for tst_id in the tmp file to generate the test template'''
                  tst["product"] = row['Family']
                  tst["test_id"] = test_id
                  tst["Comment"] = row['Common Test'].split("(")[0]
                  tst["state_id"] = states['State']
                  '''test_id,Comment,state_id for state_id in the tmp file to generate the state template'''
                  state["state_id"] = states['State']
                  state["product"] = row['Family']
                  state["Comment"] = row['Common Test'].split("(")[0]
                  state["state_regex"] = states['States Regex'] 
                  build_id(tst)
                  build_state(state)
file.close()