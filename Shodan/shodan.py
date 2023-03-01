import json
import pprint
import netaddr

pp = pprint.PrettyPrinter(indent=4)
 

with open("shodan_export.json", "r") as io:
    data = io.readlines()

new = [json.loads(i) for i in data]

valid = list()
invalid = list()

for i in new:
    for key in i.keys():
        if key == "ssl":            
            if i["ssl"]["cert"]:
                if i["ssl"]["cert"]["expired"]== True:
                    invalid.append(i)
                else:
                    valid.append(i)
          
                    
# with open("invalid_ssl.json", "w") as io: json.dump(invalid,io)
# print("invalid", len(invalid))
# with open("valid_ssl.json", "w") as io: json.dump(valid,io)
# print("valid", len(valid))

ip_addr = list()

# Addresses are not duplicated
for i in invalid:
    ip_addr.append(str(netaddr.IPAddress(i["ip"])))

ip_addr.sort()

print(type(ip_addr))
with open("invalid_ssl_ips.txt", "w") as io: 
    for i in ip_addr:
        io.writelines(i+"\n") 

