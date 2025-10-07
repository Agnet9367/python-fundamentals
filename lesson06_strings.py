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
print("Lowercase: ", random_phrase.capitalize()) #makes first letter capital and every other lowercase


