#Challange 1
#   procedure add(num1, num2)
#   display(num1 + num2)
#   procedure subtract(num1, num2)
#   display(num1 - num2)
#   procedure divide(num1, num2)
#   display(num1 / num2)
#   procedure multiply(num1, num2)
#   display(num1 * num2)
def add(num1, num2):
    print(num1 + num2)
add(1, 2)

def subtract(num1, num2):
    print(num1 - num2)
subtract(5, 5)

def divide(num1, num2):
    print(num1 / num2)
divide(6, 3)

def multiply(num1, num2):
    print(num1 * num2)
multiply(2, 5)

#Challange 2
#   procedure average(num1, num2, num3)
#   return(num1 + num2 + num3)/3
def average(num1, num2, num3):
    return(num1 + num2 + num3)/3
print(average(5,10,0))

#Challange 3
def is_even(num1):
    num1 = num1 % 2
    if num1 == 1:
        return("Odd")
    else:
        return("Even")
print(is_even(7))

#Challange 4
def analyze_word(string):
    VowelCount = 0
    ConsonantCount = 0
    for i in range(len(string)):
        if  string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u" or string[i] == "A" or string[i] == "E" or string[i] == "I" or string[i] == "O" or string[i] == "U":
            VowelCount += 1
        else:
            ConsonantCount += 1
    return(f"This word has {VowelCount} vowels and {ConsonantCount} consonants!")

print(analyze_word("word"))






    



