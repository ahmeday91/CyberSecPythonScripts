import ping3

host = input("Enter a host to ping [e.g. google.com]: ")
response_time = ping3.ping(host)
if response_time is None:
	print(host, " was unreachable")
else:
	print("Response time: ", response_time)

