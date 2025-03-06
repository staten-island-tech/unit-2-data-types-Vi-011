number1 = int(input("number 1")) 
number2 = int(input("insert number 2"))
GCF = 0

for i in range(1,number1):
    if number1 % i ==0  and number2 % i == 0:
        GCF = i
print(GCF)