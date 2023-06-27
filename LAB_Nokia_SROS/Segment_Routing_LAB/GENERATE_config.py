from Nokia_connect import *
import pandas as pd
import re
def generate_config_vprn(file_name,vprn_id):
    vprn_commands={}
    txt_file_name='./Template_config/vprn_service_commands.txt'
    df = pd.read_excel(file_name)
    # Create vprm commands
    with open(txt_file_name,'r') as file:
        content=file.read()
        for index, row in df.iterrows():
            new_content=content.replace('{vprn_id}',str(vprn_id))
            new_content=new_content.replace('{sys_ip}',row['sys_ip'])
            new_content=new_content.replace('{node_id}',str(row['Node_ID']))
            commands=[i.strip() for i in new_content.splitlines()]
            vprn_commands[row['hostname']]=commands
    return vprn_commands

def generate_config_FlexAgo(file_name,FlexAgo_name,FlexAgo_id):
    FlexAgo_commands={}
    txt_file_name='./Template_config/FlexAgo_config.txt'
    df = pd.read_excel(file_name)
    # Create vprm commands
    with open(txt_file_name,'r') as file:
        content=file.read()
        for index, row in df.iterrows():
            new_content=content.replace('{FlexAgo_name}',FlexAgo_name)
            new_content=new_content.replace('{flexago_id}',str(FlexAgo_id))
            new_content=new_content.replace('{FlexAgo_Node_id}',str(row['FlexAgo_Node_id']))
            commands=[i.strip() for i in new_content.splitlines()]
            FlexAgo_commands[row['hostname']]=commands
    return FlexAgo_commands

def generate_config_lsp_sr_te(file_name,lsp_type="dynamic/strict/loose",lsp_path=""):
    lsp_commands={}
    df = pd.read_excel(file_name)
    # Get router name and system ip
    name_sys_ip={}
    for index, row in df.iterrows():
        name_sys_ip[row['hostname']]=row['sys_ip']
    if lsp_type== 'dynamic':
        txt_file_name='./Template_config/config_dynamic_lsp_sr_te.txt'
        with open(txt_file_name,'r') as file:
            content=file.read()
            for index, row in df.iterrows():
                
                total_commands=[]
                for i in name_sys_ip:
                    if i==row['hostname']:
                        pass
                    else:
                        new_content=content.replace('{lsp_name}',f'dyn_sr_te_lsp_to_{i}')
                        new_content=new_content.replace('{far_end_system_ip}',str(name_sys_ip[i]))
                        commands=[i.strip() for i in new_content.splitlines()]
                        total_commands+=(commands)
                lsp_commands[row['hostname']]=total_commands
    elif lsp_type== 'strict':
        commands=[]
        n=1
        path_ip={name.split('-')[0]:name_sys_ip[name] for name in name_sys_ip}
        path_list=lsp_path.split('_')
        source_node_name= [name for name in name_sys_ip if path_list[0] in name][0] 
        commands.append(f'/configure router mpls path strict_lsp_{lsp_path}')
        for i in path_list:
            if i ==path_list[0] or i == path_list[-1]:
                pass
            else:
                commands.append(f'/configure router mpls path strict_path_{lsp_path} hop {n} {path_ip[i]} strict')
                n+=1
        commands.append(f'/configure router mpls path strict_path_{lsp_path} no shutdown')
        commands.append(f'/configure router mpls lsp strict_sr_te_lsp_{lsp_path} sr-te to {path_ip[path_list[-1]]}')
        commands.append(f'/configure router mpls lsp strict_sr_te_lsp_{lsp_path} path-computation-method local-cspf')
        commands.append(f'/configure router mpls lsp strict_sr_te_lsp_{lsp_path} max-sr-labels 8 additional-frr-labels 2')
        commands.append(f'/configure router mpls lsp strict_sr_te_lsp_{lsp_path} primary strict_path_{lsp_path}')
        commands.append(f'/configure router mpls lsp strict_sr_te_lsp_{lsp_path} no shutdown')
        
        lsp_commands[source_node_name]=commands
    else:
        pass
    return lsp_commands
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
if __name__ == "__main__":
    device_info=get_connect_info_from_excel_file('router_info.xlsx')
    commands=generate_config_vprn('router_info.xlsx',4)
    # commands=generate_config_lsp_sr_te('router_info.xlsx',lsp_type="strict",lsp_path="R5_R6_R2_R4_R3")
    # source_strict_lsp=list(commands.keys())[0]
    # output=ssh_and_config(device_info[source_strict_lsp],commands[source_strict_lsp]) 
    # print(output)
    # print(commands)
    # print(list(device_info.keys()))
    # fix_commands=['admin save']
    # # print(commands)
    for i in device_info:
        output=ssh_and_config(device_info[i],commands[i]) 
        print(output)