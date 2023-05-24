import requests
import json
requests.packages.urllib3.disable_warnings()  #Disable canh bao lien quan den ssl
baseUrl = "https://api.meraki.com/api/v1"
api_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
def get_org():
    url = baseUrl + "/organizations"
    header = {
        "X-Cisco-Meraki-API-Key" : api_key
    }
    response= requests.get(url,headers=header,verify=False)
    data=response.json()
    parse_data=json.dumps(data,indent=4)
    #print(parse_data)
    for i in data:
        id_org=i["id"]
        print(id_org)
if __name__ == "__main__":
    get_org()
