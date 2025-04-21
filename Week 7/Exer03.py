#create a list called log_lines and store 4 log entries
log_lines = [ "INFO User admin logged in",
                "ERROR Failed login attempt",
                "INFO User guest logged out",
                "ERROR Unauthorized access attempt",
                "ERROR in this program",
                "How are you?"]

#Create a new list

error_lines = []

#Use a for loop to check the word error in the items of the list

for element in log_lines:
    if "ERROR" in element:
        error_lines.append(element)

#print the new populated list using another for loop
for new_element in error_lines:
    print(new_element)

#print the number of elements in the list using the len()
    print("number of elements with the word 'ERROR' is", len(error_lines))
