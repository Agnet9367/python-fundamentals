# Basic strings and indexes:
greeting = "Hello"
name = "Arsen"
print(greeting, name)

# 0 1 2 3 4
# H e l l o
print(greeting[1])

# 0 1 2 3 4 
# A r s e n
print(name[4])

my_message = greeting + " " + name + "!?!?!"
print("Concatenated message: ", my_message)

word = "Supercalifragilisticalidocious"
print("Second letter: ", word[1])
print("Last letter: ", word[-1])
print("Range of letters: ", word[0:5])
print("Range of letters: ", word[:5]) # You don't need to include the 0
print("Range of letters: ", word[9:13])
print("Range of letters: ", word[0:-3])
print("Range of letters: ", word[-7:])
print("Step through every second character: ", word[::2])

# Built in functions
country = "Italy"
length_of_word = len(country)
print(length_of_word)

random_phrase = "sPOngEbOb"
print("Uppercase: ", random_phrase.upper())
print("Lowercase: ", random_phrase.lower())
print("Capitalized first letter: ", random_phrase.capitalize()) #makes first letter capital and every other lowercase
print("Title format: ", random_phrase.title())

print()

#Find and replace text
sentence = "I'm Arsen"
new_sentence = sentence.replace("I'm", "You're")
print(sentence)
print(new_sentence)

print("\n --- formatted Strings ---")
name1 = "Arsen"
age1 = 15
city1 = "New York"

print(f"Hello, my name is {name1}. I am {age1} years old and I live in {city1}")

# f-strings can do math and function calls inside {}
print(f"Next year I'll be {age1 + 1}. My name is uppercase is {name1.upper()}.")

print("\n Challanges")

#Challange 1
favorite_qoute = input("Enter your favorite qoute: ")

print(f"Your qoute is {len(favorite_qoute)} characters long")

#Challange 2
fname = input("Whats your first name?")
lname = input("Whats your last name?")
print(f"formated name: {lname}, {fname}")

#Challange 3
rword = input("Enter any word you want \n")
print("Uppercase: ", rword.upper())
print("Lowercase: ", rword.lower())
print("Backwards: ", rword[::-1])
