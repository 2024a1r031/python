#wap to take a word and print it in reverse order using slicing. Also check whether it is the same forward and backward
word = input("Enter a word: ")
word1 = word[::-1]
print(word1)
print("Same forward and backward: ",word==word1)