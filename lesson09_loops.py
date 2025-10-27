import time
#Loops in python
# Loops repeat a block of code until they hit a limit or condition.
# They exist to save us from typing the same line 500 times.
# Python gives us for-loops and while-loops.

# import time

# animals = ["monkey", "donkey", "goose", "Lamb"]

# for animal in animals:
#     time.sleep(1.5)
#     print("Now petting a", animal)
#     if animal == "donkey":
#         print("Hi donkey!")
# print("Now I have petted all of the animals!")

# for i in range(6):
#     print("Counting", i)

# for num in range(2, 11, 2): #Start, Stop, Step
#     print("Counting", num)


# favorite_word = "Fire"

# for letter in favorite_word:
#     print(letter, end="")
# print(" ")
# letter_list = []

# for letter in favorite_word:
#     print(letter, end="")
#     letter_list.append(letter)
#     print(letter_list)

# count = 0

# while count < 5:
#     print(f"Loopin' We are on loop #{count}")
#     count += 1
#     time.sleep(0.5)

# print("We escaped the loop!!!")

# user_input = ""

# while user_input != "exit":
#     user_input = input("Type 'exit' to escape: ")

count = 60
increment = 1

while count > 0:
    if count < 0:
        break
    count -= increment
    increment += 1

    print(count)








   





