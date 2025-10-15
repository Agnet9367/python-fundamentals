# lists 
# lists store multiple values in one variable
# they are ordered, mutable (changeable), and allow duplicates.
animals = ["horse", "blobfish", "monkey"]
numbers = [1, 3, 6, 9, 12]
mixed = ["Arsen", 67, False, 6.7]

print()
print()

#how to acces the elements of a list
print("First element: ", animals[0])
print("Second element: ", animals[1])
print("Last element: ", animals[-1])

#modifying lists
print()
animals[0] = "fox"
print(animals)

print()
#add element at end:
animals.append("glass frog")
print(animals)

#add elemt at specific index
animals.insert(3, "aye-aye")
print("Inserted one animals: ", animals)
animals.insert(1, "camel")
print("Inserted another animal: ", animals)

animals.remove("blobfish")
print(animals)

last_animal = animals.pop()
print("Removed animal: ", last_animal)
print("Remaining animals: ", animals)
