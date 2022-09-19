import pandas as pd
from Sessions.temp import *
from Sessions.modules import *
import re,sys

cert = []
test = []
stater = []

class sheetData():
    def __init__(self, sheet_name,test_id) -> None:
        self.test_id = test_id
        df = pd.read_excel(sys.argv[1], sheet_name)
        self.data = pd.DataFrame(df, columns=['TEST ID', 'Common Test', 'Family', 'Object ID', 'Object Command'])
        self.data = self.data.where(self.data['TEST ID'] == test_id)
        self.states_data = pd.DataFrame(df, columns=['State', 'States Regex'])
        self.family_data = pd.DataFrame(df, columns=['Family'])
        self.data = self.data.reset_index()
        self.states_data = self.states_data.reset_index()
        self.data = self.data.fillna(0)
        self.states_data = self.states_data.fillna(0)
        self.sheet_info()

    def sheet_info(self):
        state = {}
        tst = {}
        crt = {}
        '''Grep For The Common Test to Common State'''
        for index, row in self.data.iterrows():
            #self.excelData = {self.data['TEST ID']: row['Common Test'][-5:-1]}
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
                
                for index_state, states in self.states_data.iterrows():
                    if states['State'] != 0 and Common_Test != 0 :
                        states_val = states['State'][-4:]
                        if states_val == Common_Test:
                                if fam == "junos":
                                    crt["test_id"] = self.test_id
                                    crt["Comment"] = row['Common Test'].split("(")[0]
                                    tst["product"] = row['Family']
                                    tst["test_id"] = self.test_id
                                    state["product"] = row['Family']
                                    state["state_id"] = tst["state_id"] = states['State']
                                    tst["Comment"] = row['Common Test'].split("(")[0]
                                    state["Comment"] = row['Common Test'].split("(")[0]
                                    state["state_regex"] = states['States Regex']
                                    cert.append(crt)
                                    test.append(tst)
                                    stater.append(state)
                                else:
                                    crt["test_id"] = self.test_id
                                    crt["Comment"] = row['Common Test'].split("(")[0]
                                    tst["product"] = row['Family']
                                    tst["test_id"] = self.test_id
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