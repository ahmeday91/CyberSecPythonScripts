# Script to check if the given input is an octet. repeat until correct
correct_octet = False
str_octet = input("Enter an Octet <0 - 255>")
# use a loop
while correct_octet == False:
    if str_octet.isdigit() == True:
        octet = int(str_octet)
        if octet >= 0 and octet <= 255:
                correct_octet = True
        if correct_octet == False:
            str_octet == False:
(str_octet) = input("Please enter an octet <0 to 255>")
    # once the correct octet value is entered print the following
    print("The value of the octet entered is: ", str_octet)