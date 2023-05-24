from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host= "10.18.8.143",
    port= "830",
    username = "admin",
    password = "admin",
    hostkey_verify = False
)

# print("#Supported Capabilities (YANG models):")
# for capability in m.server_capabilities:
#     print(capability)

# netconf_reply = m.get_config(source="running")
# print(netconf_reply)
# print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# netconf_filter = """
# <filter>
#     <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
#         <interface></interface>
#     </interfaces>
# </filter>
# """
# netconf_reply = m.get_config(source = 'running', filter = netconf_filter)
# #print(type(netconf_reply.xml))# str
# print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# netconf_filter = """
# <filter>
#     <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
# </filter>
# """
# netconf_reply = m.get_config(source="running", filter=netconf_filter)
# print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# netconf_hostname = """
# <config>
#   <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
#      <hostname>SILVER-ducpv</hostname>
#   </native>
# </config>
# """
# netconf_reply = m.edit_config(target="running", config=netconf_hostname)
# print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# netconf_loopback = """
# <config>
#  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
#   <interface>
#    <Loopback>
#     <name>50</name>
#     <description>[Student Name]\'s loopback</description>
#     <ip>
#      <address>
#       <primary>
#        <address>10.5.50.1</address>
#        <mask>255.255.255.0</mask>
#       </primary>
#      </address>
#     </ip>
#    </Loopback>
#   </interface>
#  </native>
# </config>
# """
# netconf_reply = m.edit_config(target="running",config=netconf_loopback)
# print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())