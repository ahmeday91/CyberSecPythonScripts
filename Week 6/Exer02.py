log_entry = input("Enter a log entry of several words.")
#check for word error or failed in the string
if "error" in log_entry or "failed" in log_entry:
    print("Potential issue detected")
else:
    print("Log entry is clean")
