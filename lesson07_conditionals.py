# Cnditionals in python
# Comparison operators: ==, !=, <, >, <=, >=
# Logical operators: and, or, not
# Control flow: if, elif, else

print(67 == 76)
print("six" == "seven")
print( 6 != 7)
print(6 > 7)

#if 
#if elif else 
num1 = 67
if num1 == 67:
    print("Your number is equal to 67")

num2 = 76
if num2 == 67:
    print("Your number is equal to 67")

num3 = 6
if num3 <= 12:
    print("Your number is less than or equal to 12")
else:
    print("Your number is greater than 12")

num4 = 67
if num4 <= 12:
    print("Your number is less than or equal to 12")
else:
    print("Your number is greater than 12")

temp1 = 67
if temp1 > 80:
    print("It's hot!")
elif temp1 >= 60:
    print("It's nice!")
else:
    print("Ir's cold!")


temp2 = 46
if temp2 > 80:
    print("It's hot!")
elif temp2 >= 60:
    print("It's nice!")
else:
    print("Ir's cold!")

temp3 = 46
if temp3 > 80:
    print("It's hot!")
elif temp3 >= 60:
    print("It's nice!")
else:
    print("Ir's cold!")


x = 7
y = 4
if x == y:
    print("x is equal to y")
elif x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("error")



x1 = 7
y1 = 7
if x1 == y1:
    print("x is equal to y")
elif x1 > y1:
    print("x is greater than y")
elif x1 < y1:
    print("x is less than y")
else:
    print("error")

# logical operator: and
# both sides of the 'and' must  be true, otherwise it's false. 

age1 = 18
has_permission = True
if age1 >= 17 and has_permission:
    print("You can drive!")
else:
    print("You can't drive yet!")


age2 = 16
has_permission = True
if age2 >= 17 and has_permission:
    print("You can drive!")
else:
    print("You can't drive yet!")

day = "Wednesday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend")
else:
    print("It's the weekday")

if day is not "Monday":
    print("It's not Monday")






