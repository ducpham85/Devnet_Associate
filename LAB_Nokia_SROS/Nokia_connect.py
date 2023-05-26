from netmiko import *
from pysros.management import connect
from pysros.exceptions import *
from datetime import datetime
import sys
import json

def ssh_and_get(ip,username,password,port,command=[]):
    device={
        "device_type":"nokia_sros",
        "ip":ip,
        "username":username,
        "password":password,
        "port":port
    }
    try:
    #6. Connect to device
        CON=ConnectHandler(**device)
        info=""
        for i in command:
            info += i + '\n' + CON.send_command(i) + '\n'
    #8.Disconnect the session
        CON.disconnect()
        with open('logs.txt','a') as file:
            file.write(f'{ip} port {port} {datetime.now()} SSH Connection OK' + '\n')
        #print(info)
        return info
    except NetmikoTimeoutException:
        error = f'{ip} port {port} {datetime.now()} SSH Connection Timeout. Please check the hostname, IP, TCP port, firewall, and device availability.'
        with open('logs.txt','a') as file:
            file.write(error + '\n')
        return ""
    except NetmikoAuthenticationException:
        error = f'{ip} port {port} {datetime.now()} SSH Authentication to device failed. Check correct usename/password.'
        with open('logs.txt','a') as file:    
            file.write(error + '\n')
        return ""
def ssh_and_config(ip,username,password,port,command=[]):
    device={
        "device_type":"nokia_sros",
        "ip":ip,
        "username":username,
        "password":password,
        "port":port
    }
    try:
    #6. Connect to device
        CON=ConnectHandler(**device)
        info=CON.send_config_set(command)
    #8.Disconnect the session
        CON.disconnect()
        with open('logs.txt','a') as file:
            file.write(f'{ip} port {port} {datetime.now()} SSH Connection OK' + '\n')
        #print(info)
        return info
    except NetmikoTimeoutException:
        error = f'{ip} port {port} {datetime.now()} SSH Connection Timeout. Please check the hostname, IP, TCP port, firewall, and device availability.'
        with open('logs.txt','a') as file:
            file.write(error + '\n')
        return ""
    except NetmikoAuthenticationException:
        error = f'{ip} port {port} {datetime.now()} SSH Authentication to device failed. Check correct usename/password.'
        with open('logs.txt','a') as file:    
            file.write(error + '\n')
        return ""
def api_get(ip,username,password,port,api_url):
    try:
        connection_object = connect(host=ip,
                                    port=port,
                                    username=username,
                                    password=password,
                                    hostkey_verify=False
                                    )
    #The User need to enable netconf in "config system security user admin access" context
        pysros_ds=[]
        for i in api_url:
            output=connection_object.running.get(i,defaults=True)
            pysros_ds.append(output)
        connection_object.disconnect()
        return pysros_ds
    except RuntimeError as error1:
        print("Failed to connect.  Error1:", error1)
    except ModelProcessingError as error2:
        print("Failed to create model-driven schema.  Error:", error2)
    except Exception as error3:  # pylint: disable=broad-except
        print("Failed to connect.  Error:", error3)

    
# show_command=['/show router interface "system"','/show port']
# print(ssh_and_get("10.18.8.143","admin","admin",9027,show_command))
# config_command=["/configure router interface python_test","address 192.168.1.100/32","loopback"]
# print(ssh_and_config("10.18.8.143","admin","admin",9027,config_command))
url=["/nokia-conf:configure/router",'/nokia-state:state/port[port-id="1/1/1"]']
print(api_get("10.18.8.143","admin","admin",830,url)[0])