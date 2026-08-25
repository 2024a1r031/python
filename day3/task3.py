#wap to take an amount in rupees and calculate how many 500 and 100 notes are needed.   Output:- 3800 = 7 notes of 500 and 3 notes of 100
amount = int(input())
notes_500 = amount//500
remaining = amount%500
notes_100 = remaining//100
print(f"{amount} = {notes_500} notes of 500 and {notes_100} notes of 100")