from Nokia_connect import *
# Import pandas library to read excel file
import pandas as pd


def get_connect_info_from_excel_file(file_name):
    df = pd.read_excel(file_name)
    list_connection = {}
    for index, row in df.iterrows():
        hostname = row['hostname']
        ip_address = row['ip_address']
        username = row['username']
        password = row['password']
        port = row['port']
        sys_ip1 = row['sys_ip']
        # 5.Declare a device information to connect to
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


if __name__ == "__main__":
    excel_file_name = 'router_info.xlsx'
    txt_file_name = './Template_config/get_adj_sid.txt'
    fix_command = []
    list_interface = {}
    commands = {}
    adj_sid_info = {}
    connect_info = get_connect_info_from_excel_file(excel_file_name)
    # Lay thong tin interface name cua cac router
    # for i in connect_info:
    #     list_interface[i]=get_interface_name(connect_info[i])
    # #Lay lenh tu file
    with open(txt_file_name, 'r') as file:
        for line in file:
            # Process the line and append it to the list
            fix_command.append(line.strip())
    test_time = datetime.now()
    save_log_file = txt_file_name.split('/')[2].split('.')[0]
    log_file_name = f'{save_log_file}_{test_time.year}{test_time.month}{test_time.day}_{test_time.hour}{test_time.minute}{test_time.second}.txt'
    log_file_path = "./Logs/" + log_file_name
    print(log_file_path)
    with open(log_file_path, 'w') as file:
        for i in connect_info:
            file.write(f'show commands on Router {i} at {datetime.now()}\n')
            output = ssh_and_get(connect_info[i], fix_command)
            output1 = output.splitlines()
            Ingress_Label = [i.split(':')[1].split()[0] for i in output1 if 'Ingress Label     :' in i]
            Interface = [i.split(':')[1].strip() for i in output1 if 'Interface         :' in i]
            # [x for x in numbers if x % 2 == 0]
            adj_sid_info[i] = {k: v for k, v in zip(Interface, Ingress_Label)}
            # combined_dict = {k: v for k, v in zip(keys, values)}
            file.write(output)
            file.write(f'{i}:{adj_sid_info[i]}\n')
    print(adj_sid_info)
