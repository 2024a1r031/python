# wap to take 2- digit no as input and print the sum of its digits    Output = 57 = 5 + 7 = 12
num = int(input())
first = num//10
second = num%10
sum = first+second
print(f"{num} = {first} + {second} = {sum}")