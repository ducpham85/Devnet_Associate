import json
import requests
requests.packages.urllib3.disable_warnings()

def get_restconf_service():
    url = "https://10.215.28.72/restconf"
    headers = {
        "Content_Type":"application/yang-data+json",
        "Accept": "application/yang-data+json"
    }
    basicAuth = ("admin","admin")
    respon = requests.get(url, headers=headers, auth=basicAuth, verify=False)
    print(json.dumps(respon.json(),indent=4))
get_restconf_service()

print("#################################################################################")

# def get_restconf_interfaces():
#     url = "https://10.215.28.72/restconf/data/ietf-interfaces:interfaces"
#     headers = {"Content_Type":"application/yang-data+json","Accept": "application/yang-data+json"}
#     basicAuth = ("admin","admin")
#     respon = requests.get(url, headers=headers, auth=basicAuth, verify=False)
#     #print(json.dumps(respon.json(),indent=4))
#     print(respon.text)
# get_restconf_interfaces()

# print("#################################################################################")

def dat_loopback(): 
    api_url = f"https://10.215.28.72/restconf/data/ietf-interfaces:interfaces/interface=Loopback60"
    
    headers = { "Accept": "application/yang-data+json",
                "Content-type":"application/yang-data+json"
            }
    basicAuth = ("admin","admin")
    
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback60",
            "description": "[Duc\'s Name] loopback interface",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "10.8.60.1",
                        "netmask": "255.255.255.0"
                    }
                ]
            },
            "ietf-ip:ipv6": {}
        }
    }
    
    
    resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicAuth, headers=headers, verify=False)
    
    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
    else:
        print('Error. Status Code: {} \nError message: {}'.format(resp.status_code, resp.json()))

dat_loopback()