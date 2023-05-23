from pysros.management import connect
from pysros.exceptions import *
import sys
import json
def get_connection():
    try:
        connection_object = connect(host="10.18.8.143",
                                    port=830,
                                    username="admin",
                                    password="admin",
                                    hostkey_verify=False
                                    )
        #The User need to enable netconf in "config system security user admin access" context
    except RuntimeError as error1:
        print("Failed to connect.  Error:", error1)
        sys.exit(-1)
    except ModelProcessingError as error2:
        print("Failed to create model-driven schema.  Error:", error2)
        sys.exit(-2)
    return connection_object

if __name__ == "__main__":
    connection_object = get_connection()
    print(connection_object)
    #Output OK: <pysros.management.Connection object at 0x000001CC4E8ECC90>
