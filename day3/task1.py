#wap to take total minutes as input and convert it into hours and remaining minutes.
a = int(input())
hours = a//60
minutes = a%60
print(f"{a} minutes = {hours} hours and {minutes} minutes")