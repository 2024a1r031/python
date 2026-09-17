#wap to count how many times a particular element appears in a list.
n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)
element = int(input("Enter element to count: "))
count = 0
for num in numbers:
    if num == element:
        count = count + 1
print("The element appears", count, "times.")