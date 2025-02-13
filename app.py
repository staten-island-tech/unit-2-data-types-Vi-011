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


def calculate_tip(bill, rating):
 
    tip_percentages = {
        "bad": 0,
        "okay": 0.15,
        "good": 0.20,
        "great": 0.25
    }
    if rating not in tip_percentages:
        return "Invalid rating. Please choose from 'bad', 'okay', 'good', or 'great'."
    
    tip_percentage = tip_percentages[rating]
    
    tip = bill * tip_percentage
    
    return f"The tip for a {rating} service on a ${bill:.2f} bill is: ${tip:.2f}"


