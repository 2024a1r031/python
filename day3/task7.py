#wap to take input from the user without typecasting and multiply it by 3. Then typecast the same input to int and multiply it by 3. Print both results to show thw difference.
num = input("Enter a number: ")

result1 = num * 3

num = int(num)
result2 = num * 3

print(result1)
print(result2)