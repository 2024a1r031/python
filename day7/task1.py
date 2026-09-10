#wap to find the perfect number.
num = int(input("Enter a number: "))
divisor_sum = 0
for i in range(1,num):
    if num % 1==0:
        divisor_sum+=i
if divisor_sum==num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is NOT a perfect number")