from platform import platform
import requests,re
import lxml.html
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
from xml.etree import ElementTree as ET


def Gecko(url:str, execPath="./geckodriver"):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options, executable_path=execPath)
    driver.get(url)
    time.sleep(10)
    html = driver.page_source

    return html 

def dbg(msg: str):
    '''
    Print Message to the Console
    params:
        msg: Type str
        rtype: None
    '''
    print(f'[*] {msg}')


def platform(url):
    scrape = lxml.html.fromstring(Gecko(url))
    Affected_platform = scrape.xpath('//label[text()="Product Affected"]/following-sibling::lightning-formatted-rich-text/span/text()')[0]
    Products = re.findall(r'Affected platforms:\s+?(.*)', Affected_platform)[0].replace(' ','').split(',')        
    dbg(f"Affected Products => {Products}")

def Adv(cve_number):
    Nvd_url = f"https://nvd.nist.gov/vuln/detail/{cve_number}"
    adv_content=requests.get(Nvd_url).text
    
    
    if ":juniper:junos:" in adv_content:
        print ("The CVE is Belongs To Juniper")
        try:
            jun_adv = re.findall(r'(https?://kb\.juniper\.net/[\S]?JSA\d+)"?', adv_content)[0]
        except IndexError:
            jun_adv = re.findall(r'https?://kb\.juniper\.net/\S+(JSA\d+)"?', adv_content)[0]
        dbg(f"NVD Link => {Nvd_url}")
        dbg(f"Advisory Link => {jun_adv}")
    elif ":cisco:ios:" in adv_content:
        print("This CVE is Belongs to Cisco IOS")
        try:
            Cisco_adv = re.findall(r'https?://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/\S+"', adv_content)[0]
        except IndexError:
            dbg(help.format(cve_number, cve_number))
            Cisco_adv = input('Please Provide Advisory ID : ')
        dbg(f"NVD Link => {Nvd_url}")
        dbg(f"Advisory Link => {Cisco_adv}")
    elif ":cisco:ios_xe:" in adv_content:
        print("This CVE is Belongs to Cisco IOSXE")
        try:
            Cisco_iosxe_adv = re.findall(r'https?://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/\S+"', adv_content)[0]
        except IndexError:
            dbg(help.format(cve_number, cve_number))
            Cisco_iosxe_adv = input('Please Provide Advisory ID : ')
        dbg(f"NVD Link => {Nvd_url}")
        dbg(f"Advisory Link => {Cisco_iosxe_adv}")
    elif ":cisco:adaptive_security_appliance_software:" in adv_content:
        print("This CVE is Belongs to Cisco ASA")
    elif ":cisco:firepower_threat_defense:" in adv_content:
        print("This CVE is Belongs to FTD")
    elif ":cisco:nx-os:" in adv_content:
        print("This CVE is Belongs to NXOS")

    platform(jun_adv)
    dbg('Generating Template ...')
    
def CVE(cve_number):
    Adv(cve_number)