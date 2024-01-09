from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
from pysros.management import connect
from pysros.exceptions import *
from datetime import datetime


def ssh_and_get(device_info={}, command=[]):
    device = device_info
    try:
        # 6. Connect to device
        CON = ConnectHandler(**device)
        info = ""
        for i in command:
            output = CON.send_command(i)
            info += i + '\n' + output + '\n'
            # time.sleep(1)
            # info.append(output)
        # 8.Disconnect the session
        CON.disconnect()
        with open('logs.txt', 'a') as file:
            file.write(f'{device["ip"]} port {device["port"]} {datetime.now()} SSH Connection OK' + '\n')
        # print(info)
        return info
    except NetmikoTimeoutException:
        error = f'{device["ip"]} port {device["port"]} {datetime.now()} SSH Connection Timeout. Please check the hostname, IP, TCP port, firewall, and device availability.'
        with open('logs.txt', 'a') as file:
            file.write(error + '\n')
        return ""
    except NetmikoAuthenticationException:
        error = f'{device["ip"]} port {device["port"]} {datetime.now()} SSH Authentication to device failed. Check correct usename/password.'
        with open('logs.txt', 'a') as file:
            file.write(error + '\n')
        return ""


def ssh_and_config(device_info={}, command=[]):
    device = device_info
    try:
        # 6. Connect to device
        CON = ConnectHandler(**device)
        info = CON.send_config_set(command)
        # 8.Disconnect the session
        CON.disconnect()
        with open('logs.txt', 'a') as file:
            file.write(f'{device["ip"]} port {device["port"]} {datetime.now()} SSH Connection OK' + '\n')
        # print(info)
        return info
    except NetmikoTimeoutException:
        error = f'{device["ip"]} port {device["port"]} {datetime.now()} SSH Connection Timeout. Please check the hostname, IP, TCP port, firewall, and device availability.'
        with open('logs.txt', 'a') as file:
            file.write(error + '\n')
        return ""
    except NetmikoAuthenticationException:
        error = f'{device["ip"]} port {device["port"]} {datetime.now()} SSH Authentication to device failed. Check correct usename/password.'
        with open('logs.txt', 'a') as file:
            file.write(error + '\n')
        return ""


def api_get(ip, username, password, port, api_url):
    try:
        connection_object = connect(host=ip,
                                    port=port,
                                    username=username,
                                    password=password,
                                    hostkey_verify=False
                                    )
        # The User need to enable netconf in "config system security user admin access" context
        pysros_ds = []
        for i in api_url:
            output = connection_object.running.get(i, defaults=True)
            pysros_ds.append(output)
        connection_object.disconnect()
        return pysros_ds
    except RuntimeError as error1:
        print("Failed to connect.  Error1:", error1)
        return []
    except ModelProcessingError as error2:
        print("Failed to create model-driven schema.  Error:", error2)
        return []
    except Exception as error3:  # pylint: disable=broad-except
        print("Failed to connect.  Error:", error3)
        return []

# if __name__ == "__main__":
#     #Declare a device information to connect to
#     device_info={
#         "device_type":"nokia_sros",
#         "ip":"10.18.8.143",
#         "username":"admin",
#         "password":"admin",
#         "port":"9027"
#     }
#     command=['show router interface detail | match "If Name          :"']
#     list_interface=[]
#     output=ssh_and_get(device_info,command)
#     for i in output.splitlines()[1:]:
#         list_interface.append(i.split(':')[1].strip())
#     print(list_interface)
# show_command=['/show router interface "system"','/show port']
# print(ssh_and_get("10.18.8.143","admin","admin",9027,show_command))
# config_command=["/configure router interface python_test","address 192.168.1.100/32","loopback"]
# print(ssh_and_config("10.84.1.166","admin","admin",830,config_command))
# url=["/nokia-conf:configure/router",'/nokia-state:state/port[port-id="1/1/1"]']
# print(api_get("10.84.1.166","admin","admin",830,url))
