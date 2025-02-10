""" # Strings are for representing characters, names, words etc.
name = "David"
# Integer represents whole numbers
age = 14
# Floats represent decimals
wallet = 5.45
# Boolean represents true or false, used in evaluations
graduated = False

def add(x, y):
    print(x + y)

# input asks the user a question and stores their response as a value
bill = float(input("What was the bill?"))
# print(type(bill))
# add(40, bill)

# Lists
students = ["Joanna", "Devivid", "David", "other David", "Ethan"]
# Similar to saying for i in range(5): print(students[i])
print(students[4])
for student in students:
    print(student)

moneys = [1, 2, 3, 4, 5, 6]
total = 0
for money in moneys:
    total = total + money
    print(total)

 """

""" 
temp = 3
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold')
 """




sentence = input("Please enter a sentence: ")

def count_words (Hello, may I have a sandwhich)