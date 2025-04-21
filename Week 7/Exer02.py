#create a list called log_lines and store 4 log entries
log_lines = [ "INFO User admin logged in",
                "ERROR Failed login attempt",
                "INFO User guest logged out",
                "ERROR Unauthorized access attempt",
                "ERROR in this program",
                "How are you"]
#Use a for loop to check the word error in the items of the list
for element in log_lines:
    if "ERROR" in element:
        print(element)
