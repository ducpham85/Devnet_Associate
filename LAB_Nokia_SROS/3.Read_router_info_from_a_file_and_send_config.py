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
#5.Declare a device information to conntect to 
    device={
        "device_type":"nokia_sros",
        "ip":ip_address,
        "username":username,
        "password":password,
        "port":port
    }
#6. Connect to device
    CON=ConnectHandler(**device)
#7. Declare commands that are used for sending to the router
    config_command=["/configure router interface python_test","address 192.168.1."+str(index+1)+"/32","loopback"]
#8.Send config command to the router
    print(CON.send_config_set(config_command))
#9.Disconnect the session
    CON.disconnect()