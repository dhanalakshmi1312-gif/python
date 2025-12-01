username = input("Enter username: ")
email = input("Enter email id : ")
email_name = email.split("@")[0]

if username.isalnum() and "@" in email and "." in email and username.lower() == email_name.lower():
    print("Valid username and email id")
else:
    print("Invalid username or email id")
