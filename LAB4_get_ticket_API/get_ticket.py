import requests
import json
url="http://10.215.26.61/api/v1/ticket"
header={
    "Accept":"application/json",
    "Content-Type":"application/json"
}
body=json.dumps({
  "username": "admin",
  "password": "vnpro@123"
})
response=requests.post(url,headers=header,data=body,verify=False)
print(response.text)