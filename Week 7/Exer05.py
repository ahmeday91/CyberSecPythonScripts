ip_addresses = ["192.168.1.1",
                "10.0.0.1",
                "10.10",
                "172.16.0.1",
                "193.168.1.7",
                "a.b.c.d"]
masked_ips = []

# Take very element from the list, use the split function

for elements in ip_addresses:
    newList = elements.split(".")
    if len(newList) !=4:
        print("This is an invalid IP address")
    else:
        newList[3] = "xxx"
        maskedIp = newList[0]+ "." + newList[1] +"."+ newList[3]
        masked_ips.append(maskedIp)

#print the masked_ips
for values in masked_ips:
    print(values)