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
        command=['/admin set-time 2021/06/25 00:00:00']
        output=ssh_and_config(device,command)
        print(output)