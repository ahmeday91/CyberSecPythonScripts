import ping3

hosts = ["google.com", "rmit.edu.au", "twitter.com", "yahoo.com"]
reachable_hosts = []

#Use a loop to ping each element in the host[] list
for element in hosts:
    response_time = ping3.ping(element)
    if response_time is not None:
        element = element+" Response Time: " + str(response_time)
        reachable_hosts.append(element)
#print all the reachable_hosts

print("Folloawing are a list of REACHABLE HOSTS!")
for hosts in reachable_hosts:
    print(hosts)