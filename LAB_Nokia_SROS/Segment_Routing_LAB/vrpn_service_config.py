# Import pandas library to read excel file
import pandas as pd

from Nokia_connect import *


def get_connect_info_from_excel_file(file_name):
    df = pd.read_excel(file_name)
    list_connection = {}
    for index, row in df.iterrows():
        hostname = row['hostname']
        ip_address = row['ip_address']
        username = row['username']
        password = row['password']
        port = row['port']
        # 5.Declare a device information to conntect to
        device = {
            "device_type": "nokia_sros",
            "ip": ip_address,
            "username": username,
            "password": password,
            "port": port
        }
        list_connection[hostname] = device
    return list_connection


def get_interface_name(device_info):
    command = ['show router interface detail | match "If Name          :"']
    list_interface = []
    output = ssh_and_get(device_info, command)
    for i in output.splitlines()[1:]:
        list_interface.append(i.split()[-1].strip())
    return list_interface


def get_system_ip(device_info):
    command = ['show router interface "system" | match "system" post-lines 1']
    system_ip = ''
    output = ssh_and_get(device_info, command)
    system_ip = output.splitlines()[2].split()[0]
    return system_ip


if __name__ == "__main__":
    excel_file_name = 'router_info.xlsx'
    txt_file_name = 'vprn_service_commands.txt'
    fix_command = []
    list_interface = {}
    system_ip = {}
    commands = {}
    connect_info = get_connect_info_from_excel_file(excel_file_name)
    # #Lay thong tin interface name cua cac router
    # for i in connect_info:
    #     list_interface[i]=get_interface_name(connect_info[i])
    # Lay thong tin system_ip cua cac router
    for i in connect_info:
        system_ip[i] = get_system_ip(connect_info[i])
    # Lay lenh tu file
    with open(txt_file_name, 'r') as file:
        for line in file:
            # Process the line and append it to the list
            fix_command.append(line.strip())

    for i in system_ip:
        commands[i] = fix_command
        last_block_ip = system_ip[i].split('.')[3]
        rd_first_part = system_ip[i].split('/')[0]
        flex_commands = []
        flex_commands.append(f'/route-distinguisher {rd_first_part}:3')
        flex_commands.append(f'/configure service vprn 3 interface lo1 address 3.3.3.{last_block_ip}')
        print(flex_commands)
        commands[i] += flex_commands
    print(commands['R5-MTC1'])
    # for i in connect_info:
    #     output=ssh_and_config(connect_info[i],commands[i]) 
    #     print(output)
