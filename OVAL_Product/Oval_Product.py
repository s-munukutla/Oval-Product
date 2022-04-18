ximport pandas as pd
"""Declaring The Sheet Name And Test ID Manually"""

sheet_info = str(input("Enter  The Sheet Name:"))
file = open('Product.txt', 'w')
df = pd.read_excel('/home/surya/Documents/Python/OVAL_Product/Definition ID Database.xlsx', sheet_info)

while True:
   test_id = str(input("Enter the Test Id:"))
   if test_id == '0':
          break;
   data = pd.DataFrame(df,columns=['TEST ID','Common Test','Family','Object ID','Object Command'])
   data = data.where(data['TEST ID'] == test_id)
   states_data = pd.DataFrame(df,columns=['State', 'States Regex'])
   data = data.reset_index()
   states_data=states_data.reset_index()
   data=data.fillna(0)
   states_data=states_data.fillna(0)
   '''Grep For The Common Test to Common State'''
   for index, row in data.iterrows():
      if row['Common Test'] != 0:
         Common_Test = row['Common Test'][-5:-1]
         for index_state, states in states_data.iterrows():
            if states['State'] != 0 and Common_Test != 0 :
               states_val = states['State'][-4:]
               if states_val == Common_Test:
                  save = [row['TEST ID']+"\t",row['Common Test']+"\t",states['State']+"\t",states['States Regex']+"\t"]
                  file.writelines(save)
                  file.write('\n')
file.close()     
             
