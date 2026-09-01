#wap to take a student's full name and display:   -total no of characters   -first ch   -last ch   -name in uppercase
name = input("name: ")

print("Total number of characters:", len(name))
print("First character:", name[0])
print("Last character:", name[-1])
print("Name in uppercase:", name.upper())