#1. Import pandas library to read excel file 
import pandas as pd
#2.Import ConnectHander method from the netmiko library
from netmiko import ConnectHandler
#3.Load the router information from an Excel file
df = pd.read_excel('router_info.xlsx')
#4.Iterate over the rows of the dataframe and connect to each router
for index, row in df.iterrows():
    hostname = row['hostname']
    ip_address = row['ip_address']
    username = row['username']
    password = row['password']
    port=row['port']
#5.Declare a divice information to conntect to 
    device={
        "device_type":"nokia_sros",
        "ip":ip_address,
        "username":username,
        "password":password,
        "port":port
    }
#6. Connect to device
    CON=ConnectHandler(**device)
    
#7.Send command to the rouuter and get information
    print(CON.send_command('show system information | match "System Name"'))
#8.Disconnect the session
    CON.disconnect()