#wap to take a student name and roll number, then generate a username using first 3 letters of the name and last 2 digits of the roll number
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# username = name[0] + name[1] + name[2] + roll_no[-2] + roll_no[-1]
username = name[:3] + roll_no[-2:]
print("Username:", username)
