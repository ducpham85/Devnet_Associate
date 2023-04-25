import ruamel.yaml as yaml
import json

if __name__ == "__main__":
    print('##################')
    print('###### YAML ######')
    print('##################')
    # Open the user.yaml file as read only
    with open("user.yaml", "r") as stream:
        # Load the stream using safe_load
        user_yaml = yaml.safe_load(stream)
    # Print the object type
    print("Type of user_yaml variable:")
    print(type(user_yaml))
    print('----------------------')
    # Iterate over the keys of the user_yaml and print them
    print('Keys in user_yaml:')
    for key in user_yaml:
        print(key)
    print('----------------------')
    # Create JSON structre with indents and soreted keys
    print('JSON with indents and sorted keys')
    user_json = json.dumps(user, default=str, indent=4, sort_keys=True)
    print(user_json)
    print('----------------------')
    # Print to file user.json
    file = open("user.json","w")
    file.write(user_json)
    file.close()