#ask user for a source ip address and a protocol (TCP/UDP)
ip_address = input("Please enter an ip address")
protocol = input("Enter a protocol (TCP/UDP): ")
if protocol == "TCP" and ip_address.startswith("192.168"):
    print("This is an internal TRAFFIC")
