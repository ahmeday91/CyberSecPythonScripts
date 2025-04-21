role = input("Enter your role: admin/user/guest/other: ")
if role == "admin":
    print("Access granted. Full access")
elif role == "user":
    print("Access granted. Limited access")
elif role == "guest":
    print("Access granted. Read-only access")
else:
    print("Such a role does not exist. Access denied")
