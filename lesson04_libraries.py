# Math
# Abstraction hidden code behing 
import math
print("\n--- Math Library ---\n")

print("Square root ", math.sqrt(36))
print("Round up to an integer: ", math.ceil(5.3))
print("Round down to an integer: ", math.floor(7.7))
print("Power: ", math.pow(2,6))
print("Pi:", math.pi)

# Random

seed = 132.4444
step_1 = seed / 6.7
step_2 = step_1 - 800
step_3 = step_2 + 18842
answer = step_3 
limitednumber = math.floor(answer * 10)
print("My Own Random Number Generator:", limitednumber)

import random

#methods:
print("Random integer: ", random.randint(1, 10))
print(random.random())
print(random.choice(["bread", "chicken", "cheese"]))
favorites = ["1", "2", "3"]
print(random.choice(favorites))
random.shuffle(favorites)
print(favorites)

#challenge 1
diameter = 14
radius = diameter / 2
Pi = 3.14
radius2 = radius * radius
result = math.pi * radius2
print("Area: ", result)

#challenge 2
print("Dice: ", random.randint(1, 6))
 
