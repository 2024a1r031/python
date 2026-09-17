#wap to input numbers in a list and find the second largest number.
n = int(input("Enter number of elements: "))
num = []
for i in range(n):
    num = int(input("Enter number: "))
    num.append(num)
num.sort()

print("Second largest number:", num[-2])