#1.Import ConnectHander method from the netmiko library
from netmiko import ConnectHandler
#2.Declare a divice information to conntect to 
device={
    "device_type":"nokia_sros",
    "ip":"10.18.8.143",
    "username":"admin",
    "password":"admin",
    "port":"9027"
}
#3. Connect to device
CON=ConnectHandler(**device)
#4.Send command to the rouuter
print(CON.send_command("/show router interface"))
#5.Send config to the router
print(CON.send_config_set(["/config router interface test123","address 1.1.1.1/32"]))
#6.Disconnect the session
CON.disconnect()