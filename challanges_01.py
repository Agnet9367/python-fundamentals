import math
import random


#Challange 1
word = input("Type the word to check if it is a palindrome: \n")
rword = word[::-1]
if word == rword:
    print("True")
else:
    print("False")

#Challange 2
email = input("Type your email here: \n")
part_email = email.split("@") 
print(part_email[1])

#Challange 3
list = ["orange", "blueberry", "cherry"]
if input("What is the last thing on your list?: \n") == list[-1]:
    print("True")
else:
    print("False")
    
#Challange 4
string = input("Type any word you want here: \n")
if len(string) < 3: print(string)
elif string[-3:] == "ing": print(string + "ly")
else: print(string + "ing")

