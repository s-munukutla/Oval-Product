from sheet_info import sheet_info
from Advproduct import CVE


def __init__():
    cve_number=input("Enter the CVE Number:")
    CVE(cve_number)
    sheet_inf = str(input("Enter The Sheet Name:"))
    sheet_info(sheet_inf)

__init__()