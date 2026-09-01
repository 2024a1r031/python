#wap to take a 10-digit mobile no and display only the last 4 digits. Replace the first 6 digits with ******
mobile = input("Enter 10-digit mobile number: ")
print("******" + mobile[6] + mobile[7] + mobile[8] + mobile[9])