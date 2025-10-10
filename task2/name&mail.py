username = input("Enter username: ")
email = input("Enter email id : ")

if username.isalnum() and "@" in email and "." in email:
    print("Valid username and email id")
else:
    print("Invalid username or email id")
