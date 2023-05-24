#Import the netmiko,csv library
from netmiko import *
import csv
#Declare a divice information to conntect to 
device={
    "device_type":"nokia_sros",
    "ip":"10.18.8.143",
    "username":"admin",
    "password":"admin",
    "port":"9027"
}
try:
    #Connect to device
    CON=ConnectHandler(**device)
    #4.Send command to the rouuter
    output=CON.send_command("/show port")
    # Split the output to lines 
    output=output.splitlines()
    #get only port info
    port_status=[n for n in output if "1/" in n]
    #Add detail port info to list
    list_port_status=[n.split() for n in port_status]
    #print(list_port_status)
    first_row=['Port ID','Admin State','Link','Port State', 'Config MTU', 'Oper MTU','LAG','Port Mode','Port Encp','Port Type','Optic Module']
    port_info=[first_row]
    port_info += list_port_status
    #print(port_info)
    
    #write info to csv file
    filename='./Port_Data/port_data.csv'
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(port_info)
    #6.Disconnect the session
    CON.disconnect()
except NetmikoTimeoutException as e:
    print("Connection Timeout. Please check the hostname, IP, TCP port, firewall, and device availability.")
    print(str(e))
except NetmikoAuthenticationException:
    print("Authentication to device failed. Check correct usename/password")