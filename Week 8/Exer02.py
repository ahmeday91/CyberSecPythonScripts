#include a list to store the ip addresses
hosts = []
#Ask the user for the number of IP addresses
numberOfIpAdd = int(input("How many IP addresses are there? :"))
#Use a for loop to get that many number of ip addresses
for number in range (numberOfIpAdd):
    ipAdd = input("Please enter the ip address: ")
    hosts.append(ipAdd)
    #finally print all the ip addresses from the list of hosts[]
for element in hosts:
    print(element)
    
