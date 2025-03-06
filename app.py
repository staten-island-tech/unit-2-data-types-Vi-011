""" # Strings are for representing characters, names, words etc.
name = "David"
# Integer represents whole numbers
age = 14
# Floats represent decimals
wallet = 5.45
# Boolean represents true or false, used in evaluations
graduated = False

def add(x, y)
    print(x + y)

# input asks the user a question and stores their response as a value
bill = float(input("What was the bill?"))
# print(type(bill))
# add(40, bill)

# Lists
students = ["Joanna", "Devivid", "David", "other David", "Ethan"]
# Similar to saying for i in range(5): print(students[i])
print(students[4])
for student in students
    print(student)

moneys = [1, 2, 3, 4, 5, 6]
total = 0
for money in moneys
    total = total + money
    print(total)
 """

""" 
sentence = input("Please enter a sentence: ").strip() 

def count_words(sentence):
    words = sentence.split() 
    return len(words)
word_count = count_words(sentence)
print(f"The number of words in the sentence is: {word_count}")
 """

""" 
verb1 = input("enter verb:")
verb2 = input("enter verb2:")
noun = input("enter noun:")
number = input("enter number:")
celebrity = input("enter celebrity:")

madlib = f"One day, {celebrity} decided to {verb1} and {verb2} through the snowy park. They looked up and saw a {noun} that shined very brightly. {celebrity} counted to {number} before heading to the moon."

print(madlib)

 """

""" 
day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")

 """

""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" 
number = 34
if number %2 == 0:
    print("even")
else:
    print("odd")

 """

""" 
bill = float(input("bill"))
service = input("How was the service? (bad, okay, good, great): ").lower()
tip_percentage = 0
if service == ("bad"):
      tip_percentage = 0.00
elif service == ("okay"): 
      tip_percentage = 0.15
elif service == ("good"):
      tip_percentage = 0.20
elif service == ("great"):
      tip_percentage = 0.25
tip = bill * tip_percentage
total = bill + tip
print(f"Tip amount: ${tip:.2f}")
print(f"Total bill (including tip): ${total:.2f}")
    
 """

 
 
""" number = float(input("number"))
factors = []
for i in range(1, int(number) + 1):
    if number % i == 0:
        factors.append(i)
        print("Factors of", int(number), "are:", factors) """



""" T = 0
S = 0
def add (x,y):
    print (x+y)
language = input(str("input text"))
for l in language:
    if l == "t" or l == "T":
        add(1, l)
    if l == "S" or l == "s":
        add(1, l)
print(l)
 """


number1 = int(input("number 1")) 
number2 = int(input("insert number 2"))
factors1 = []
factors2 = []
for i in range(1, int(number1) + 1):
    if number1 % i == 0:
        factors1.append(i)
print("Factors of", int(number1), "are:", factors1) 

for i in range(1, int(number2) + 1):
    if number2 % i == 0:
        factors2.append(i)
print("Factors of", int(number2), "are:", factors2)

list = []

for x in factors1:
    if x in factors2:
        list.append (x)

print(list)





#list out factors and find common ones. 
#through common factors, find the smallest number




