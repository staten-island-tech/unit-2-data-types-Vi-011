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

verb1 = input("run")
verb2 = input("sled")
noun = input("moon")
number = input("14")
celebrity = input("Lady Gaga")

madlib = f"One day, {"Lady Gaga"} decided to {"run"} and {"sled"} through the snowy park. They looked up and saw a {"moon"} that shined very brightly. {"Lady Gaga"} counted to {14} before heading to the moon."

print(madlib)

