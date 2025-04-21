#Create a list and store the 4 ip addresses
ip_address = ["192.168.1.1",
              "192.168.2.1",
              "192.168.3.1",
              "192.168.4.1"]
ip_check = input("Enter an ip address to check:")
#Check if the input is a blocked ip address
if ip_check in ip_address:
    print("This is a blocked ip address", ip_check)
else:
    print("This is not a blocked ip address", ip_check)