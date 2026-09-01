#wap to take marks of three subjects out of 100. Print True if the student scored at least 40 in all three subjects and avg marks are atleast 50.
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))

print(m1 >= 40 and m2 >= 40 and m3 >= 40 and (m1 + m2 + m3) / 3 >= 50)