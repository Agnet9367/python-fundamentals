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

animal_to_replace = animals.index("monkey")
print(animal_to_replace)

empty_list = []
empty_list.append("Thing")
print(empty_list)

nums = [3,7,4,2,6,9,1,5,8,0]
print("Length of the list: ", len(nums))
print("Min: ", min(nums))
print("Max: ", max(nums))
print("Sum: ", sum(nums))

nums.sort()
print(nums)
animals.sort()
print(animals)

if "cat" in animals:
    print("Cat is in the list!")
else:
    print("Cat is not in the list!")

original_list = [1, 2, 3]
copied_list = original_list.copy()
copied_list.append(4)
print(original_list)
print(copied_list)

matrix = [ 
    [1,2,3], 
    [4,5,6], 
    [7,8,9] 
    ]
 
print(matrix[2])
print(matrix[0][2])

#Challange 1
list2 = [1, 2, 3, 4, 5, 6]
ulist = int(input("Enter a new integer: "))
newlist = [1, 2, ulist, 4, 5, 6]
print(newlist)

#Challange 2 
shopping = []
shopping.append("potato")
shopping.append("tomato")
shopping.append("salad")
shopping.insert(2, "spices")
shopping.remove("potato")
print(shopping)




