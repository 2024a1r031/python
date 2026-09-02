#wap to take a password and check whether it contains @ and has atleast 8 characters.
password = input("Enter pass: ")
print("@" in password and len(password) >= 8)