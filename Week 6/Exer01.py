protocol = input("Please enter a protocol 'HTTPS or HTTP': ")
port1 = int(input("Enter the port number: "))
if port1.isdigit():
    port = int(port1)
    #using the AND logical operator check if encrypted
    if protocol == "HTTPS" and port == 443:
        print("This is an encrypted connection")
        print("Protocol entered is:", protocol)
        print("Port number entered is:" , port)
    else:
        print ("This is NOT an encrypted connection")
        print ("The protocol entered is", protocol)
        print ("The port entered is", port)
else:
    print("Please enter a number for PORT number")