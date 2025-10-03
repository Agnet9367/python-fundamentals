# User input
# ctrl + forward slash /
print("\n--- User Input ---")

name = input("Enter you name: ")
print(name)

age1 = input("Enter you age: ")
print("You are " + age1 + " years old")
print(type(age1))

age2 = int(input("Enter you age: "))
print("After 10 years you will be:", age2 + 10)
print(type(age2))

# Chalange 1
favorite_color = input("What's your favorite color?")
print(favorite_color, "is a nice color!")

# Chalange 2 
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print("If you add those two number you get: ", number1 + number2,)

#Challange 3
import math

diameter_circle = int(input("What is the diameter of the circle?"))
step1 = diameter_circle / 2
step2 = step1 * step1
area = step2 * math.pi
print("The area of that circle is: ", area)

# Chalange 4
import random

number_of_sides = int(input("How many sides do you want your dice to be? "))
print("You rolled: ", random.randint(1, number_of_sides))

