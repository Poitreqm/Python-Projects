#
# 1108. Defanging an IP Address
# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".
#


address = "1.1.1.1"
res = address.replace(".", "[.]")

print(res)
