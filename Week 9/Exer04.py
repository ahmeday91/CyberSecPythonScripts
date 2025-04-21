#Store and print the list of ip addresses until a "return" key is pressed
#create a blank list
ip_list = []
ip_address = input("Please enter an ip address")
#use a while loop to check and repeat
while ip_address != "":
    ip_list.append(ip_address)
    ip_address = input("Please enter an ip address")
#use a for loop to print all the ip addresses from the list
for value in ip_list:
    print(value)