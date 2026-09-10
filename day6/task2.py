#wap to take input of four numbers from the user and find the greatest number amongst them 
n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
n3 = int(input("Enter number3: "))
n4 = int(input("Enter number4: "))
if n1>n2 and n1>n3 and n1>n4:
    print("Number 1 is greatest!")
elif n2>n1 and n2>n3 and n2>n4:
    print("Number 2 is greatest!")
elif n3>n1 and n3>n3 and n3>n4:
    print("Number 3 is greatest!")
else:
    print("Number 4 is greatest!")