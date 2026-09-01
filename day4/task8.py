#wap to take an email address and print the domain name
email = input("Enter email address: ")
domain = email[email.find("@") + 1:]
print("Domain name:", domain)