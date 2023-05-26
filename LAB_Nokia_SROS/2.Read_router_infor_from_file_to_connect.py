#1. Import pandas library to read excel file 
import pandas as pd
#2.Import ConnectHander method from the netmiko library
from netmiko import *
#3.Load the router information from an Excel file
df = pd.read_excel('router_info.xlsx')
#4.Iterate over the rows of the dataframe and connect to each router
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
    try:
    #6. Connect to device
        CON=ConnectHandler(**device)
    
    #7.Send command to the router and get information
        # print(str(index+1)+"." + CON.send_command('show system information | match "System Name"'))
        # info=CON.send_command('show system information | match "System Name"')
        # info=info.split(":")
        # info[1]=info[1].strip()
        # print(info)
        info=CON.send_command('show router interface "system" | match system context all')
        info=info.split("\n")
        print(info[1])
    #8.Disconnect the session
        CON.disconnect()
    except NetmikoTimeoutException as e:
        print("Connection Timeout. Please check the hostname, IP, TCP port, firewall, and device availability.")
        print(str(e))
    except NetmikoAuthenticationException:
        print("Authentication to device failed. Check correct usename/password")
    