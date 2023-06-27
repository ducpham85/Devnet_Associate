from Nokia_connect import *
import csv
#Import pandas library to read excel file 
import pandas as pd
import re
def get_connect_info_from_excel_file(file_name):
    df = pd.read_excel(file_name)
    list_connection={}
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
        list_connection[hostname]=device
    return list_connection
def get_interface_name(device_info):
    command=['show router interface detail | match "If Name          :"']
    list_interface=[]
    output=ssh_and_get(device_info,command)
    for i in output.splitlines()[1:]:
        list_interface.append(i.split()[-1].strip())
    return list_interface
    
if __name__ == "__main__":
    excel_file_name='router_info.xlsx'
    txt_file_name='fix_ospf_config.txt'
    fix_command=[]
    list_interface={}
    commands={}
    connect_info=get_connect_info_from_excel_file(excel_file_name)
    #Lay thong tin interface name cua cac router
    for i in connect_info:
        list_interface[i]=get_interface_name(connect_info[i])
    #Lay lenh tu file
    with open(txt_file_name,'r') as file:
        for line in file:
        # Process the line and append it to the list
            fix_command.append(line.strip())  
    for i in list_interface:
        list_test=[]
        commands[i]=fix_command
        for j in list_interface[i]:
            list_test.append(f'/configure router ospf area 0 interface {j} interface-type point-to-point')
        commands[i]=fix_command+list_test
    for i in connect_info:
        output=ssh_and_config(connect_info[i],commands[i]) 
        print(output)

    