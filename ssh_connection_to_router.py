from netmiko import ConnectHandler
# declare device as dictionary
device={
    "device_type":"cisco_ios",
    "ip":"10.18.8.150",
    "username":"vnpro",
    "password":"vnpro#123",
    "secret":"vnpro#321"
}
#connect to device via ssh
CON=ConnectHandler(**device)  #unpack, truyen gia tri vao ben trong
CON.enable()

#send_config_set_function
print(CON.send_config_set("hostname R1-duc"))
CON.send_config_set(["int ethernet0/2","no shut","ip address 10.10.10.1 255.255.255.0"])
#use for loop
for i in range(1,4):
    print(CON.send_config_set(["int ethernet0/"+str(i),"no shut","ip address 10.10.10."+str(i+10)+" 255.255.255.0"]))
#send command function
print(CON.send_command("show ip int br"))
#Disconnect to device
CON.disconnect()