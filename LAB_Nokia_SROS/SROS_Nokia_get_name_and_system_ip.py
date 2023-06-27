#Import the netmiko,csv library
#from netmiko import *
from Nokia_connect import *
import csv
#Import pandas library to read excel file 
import pandas as pd
import re

if __name__ == "__main__":
    df = pd.read_excel('router_info.xlsx')
    name_ip_info=[]
    for index, row in df.iterrows():
        hostname = row['hostname']
        ip_address = row['ip_address']
        username = row['username']
        password = row['password']
        port=row['port']
    #5.Declare a device information to conntect to 
        device={
            "device_type":"nokia_sros",
            "ip":ip_address,
            "username":username,
            "password":password,
            "port":port
        }
        command=['/show system information | match "System Name"','/show router interface "system" | match system post-lines 1']
        output=ssh_and_get(device,command)
        if output==[]:
            pass
        else:
            
            system_name=""
            system_ip=""
            search_system_name=re.compile(r'System Name            :')
            match_system_name=search_system_name.search(output)
            search_system_ip=re.compile(r'Network system')
            match_system_ip=search_system_ip.search(output)
            if match_system_name:
                end_index=match_system_name.end()
                system_name=output[end_index+1:end_index+4].strip()
                
            else:
                system_name="not found"
            if match_system_ip:
                end_index=match_system_ip.end()
                system_ip=output[end_index+3:end_index+20].strip()
            else:
                system_ip="not found"
            print(f'{system_name}:{system_ip}')
