# CovertFormat

## 1. Cài đặt thư viện ruamel.yaml :
```
pip install ruamel.yaml
```
Trong phần này, bạn sẽ phát triển đoạn script Python để chuyển đổi file YAML bằng cách sử dụng module ruamel.yaml. 
Trong phần đầu đoạn code, import module ruamel.yaml
```
import ruamel.yaml import yaml
```

## 2. Đọc file YAML:

```
with open("user.yaml","r") as stream:
  user_yaml=yaml.safe_load(stream)
 ```
 Kiểm tra Kiểu dữ liệu khi đọc file YAML
 ```
 print(type(user_yaml))
 ```
 ![image](https://user-images.githubusercontent.com/129259654/233890950-a4658c41-73a6-41af-8916-47f5d005ceeb.png)

 ## 3. In key trong user_yaml:
 
 ```
  for key in user_yaml:
        print(key)
 ```
 ![image](https://user-images.githubusercontent.com/129259654/233890986-fcfb325e-299d-44ba-b360-3f9034895a05.png)

 ## 4. In giá trị trong user_yaml:
 
 Để lấy giá trị, chúng ta cần truyền key của giá trị đó
 Ví dụ cần lấy giá trị của key "id"
 ```
 print("value of key 'id':", user_yaml['id'])
 ```
 ![image](https://user-images.githubusercontent.com/129259654/233891066-85300204-27bc-45b4-bfd1-c4d0736b2a36.png)

 ## 5. Tạo cấu trúc JSON
 Sử dụng option indent để xác định khoảng lùi đầu dòng.
 
 Để sắp xếp các key theo thức tự alpha dùng sort_keys= True (mặc định là False)
 ```
 print('JSON with indents and sorted keys')
 user_json = json.dumps(user_yaml, default=str, indent=4, sort_keys=True)
 print(user_json)
 ```
 ![image](https://user-images.githubusercontent.com/129259654/233891125-b2338c18-8dbe-4450-8a79-daa9ac75cd1c.png)

 ## 6. Xuất ra file Json
 
 ```
 file = open("user.json","w")
 file.write(user_json)
 file.close()
 ```
 
  

