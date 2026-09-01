#wap to take student details like name,roll number, CGPA and hostel status from the user. Typecast them into appropriate types and print them along with their dedicated type.
name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
cgpa = float(input("Enter CGPA: "))
hostel = bool(int(input("Hostel status (1 for Yes, 0 for No): ")))

print("Name:", name, type(name))
print("Roll Number:", roll_no, type(roll_no))
print("CGPA:", cgpa, type(cgpa))
print("Hostel Status:", hostel, type(hostel))