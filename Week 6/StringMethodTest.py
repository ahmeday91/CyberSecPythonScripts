name = "RMIT IUNIVERSITY"
new_name = name.lower()
print("Original", name)
print("In Lowercase:", new_name)
#checking for startswith() function
if name.startswith("RMIT"):
    print("The string starts with RMIT")
else:
    print("Does not start with RMIT")
#using the count method
noOfChar = name.count("I")
print("Number of I's = ", noOfChar)