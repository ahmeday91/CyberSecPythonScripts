#5.	Develop a script that reads a log message that should be in the format:
#“timestamp – event_type - message”
event=input("Enter the log message in proper format:")
event_list = event.split("-")
print(event_list[2])
if len(event_list) != 3:
    print("Incorrect format, please use 'timestamp - event_type - message'")
else:
    print("Time of the event is: ", event_list[0])
    print("Event type is: ", event_list[1])
    print("Message of the event is: ", event_list[2])