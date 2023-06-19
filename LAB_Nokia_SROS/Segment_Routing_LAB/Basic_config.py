from Nokia_connect import *
import csv
#Import pandas library to read excel file 
import pandas as pd
import re

if __name__ == "__main__":
    df = pd.read_excel('router_info.xlsx')
    command=[]
    with open('Basic_command.txt','r') as file:
        for line in file:
        # Process the line and append it to the list
            command.append(line.strip())  # Remove trailing
    print(command) 
    for index, row in df.iterrows():
        hostname = row['hostname']
        ip_address = row['ip_address']
        username = row['username']
        password = row['password']
        port=row['port']
        sys_ip1=row['sys_ip']
    #5.Declare a device information to conntect to 
        device={
            "device_type":"nokia_sros",
            "ip":ip_address,
            "username":username,
            "password":password,
            "port":port
        }
        # command.append('admin save')
        # command.append(f'/configure router interface system address {sys_ip1}/32')
        # command.append(f'/configure system name {hostname}')
        # command.append('admin save')
        # print(command)
        output=ssh_and_config(device,command)
        print(output)
        # command=[]
    