#print a menu until a terminating condition is reached
completed = False
while not completed:
    #print the menu
    print("*** Menu ***")
    print("A: Option one")
    print("B: Option two")
    print("C: Quit")
    choice = input("Please enter your choice:")
    if choice == "A":
        print("You chose option one")
    elif choice == "B":
        print("You chose option two")
    elif choice == "C":
        completed = True
#after the loop message
print("The program has terminated")