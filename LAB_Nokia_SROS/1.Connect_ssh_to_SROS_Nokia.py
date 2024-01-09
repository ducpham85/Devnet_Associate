# 1.Import ConnectHandler method from the netmiko library
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException

# 2.Declare a device information to connect to
device = {
    "device_type": "nokia_sros",
    "ip": "10.18.8.143",
    "username": "admin",
    "password": "admin",
    "port": "9027"
}
try:
    # 3. Connect to device
    CON = ConnectHandler(**device)
    # 4.Send command to the router
    print(CON.send_command("/admin display-config"))
    # 5.Send config to the router
    print(CON.send_config_set(["/config router interface test123", "address 1.1.1.1/32"]))
    # 6.Disconnect the session
    CON.disconnect()
except NetmikoTimeoutException as e:
    print("Connection Timeout. Please check the hostname, IP, TCP port, firewall, and device availability.")
    print(str(e))
except NetmikoAuthenticationException:
    print("Authentication to device failed. Check correct username/password")
