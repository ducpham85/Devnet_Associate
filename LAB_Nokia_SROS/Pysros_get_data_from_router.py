from pysros.management import connect
from pysros.exceptions import *
import sys
import json
# def get_connection():
try:
    connection_object = connect(host="10.18.8.143",
                                port=830,
                                username="admin",
                                password="admin",
                                hostkey_verify=False
                                )
    #The User need to enable netconf in "config system security user admin access" context
    
except RuntimeError as error1:
    print("Failed to connect.  Error1:", error1)
except ModelProcessingError as error2:
    print("Failed to create model-driven schema.  Error:", error2)
except Exception as error3:  # pylint: disable=broad-except
    print("Failed to connect.  Error:", error3)
print("test")

# if __name__ == "__main__":
#     connection_object = get_connection()
#     #Obtaining the data from a YANG leaf  data structure
#     pysros_ds = connection_object.running.get('/nokia-state:state/port[port-id="1/1/1"]')
#     # print(pysros_ds)
#     #Obtaining the data from a YANG container data structure
#     # data_container=connection_object.running.get('/nokia-conf:configure/router[router-name="Base"]/interface[interface-name="system"]')
#     # print(data_container)
#     # data_container=dict(data_container)
#     # print(type(data_container))
#     # print(data_container["interface-name"])
#     for ident in pysros_ds.keys():
#         print(ident)