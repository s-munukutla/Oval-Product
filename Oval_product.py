from Sessions.sheet_info import sheetData 
from Sessions.Advproduct import CVE


def __init__():
    cve_number=input("Enter the CVE Number:")
    CVE(cve_number)
    sheet_info = str(input("Enter The Sheet Name:"))
    test_id=''
    sheetData(sheet_info,test_id)

__init__()