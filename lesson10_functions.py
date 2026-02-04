# Python functions are simply blocks of code that can be reused
# To run a function, you "call" the function by writing its name, followed by parenthesis, and any arguments that it needs.

print("Functions (Procedures)")
print("Example 1")
def say_hi():
    print("Hi!")
def say_bye():
    print("Bye!")


say_hi()
say_bye()
say_hi()
say_bye()

print("\nExample 2")

def express_this(e): # e is called a PARAMETER, which is a placeholder for an ARGUMENT
    return e

expression = express_this(1 + 2) # The mathmatical expression here is the Argument
print(expression)
expression2 = express_this(67 * 67)
print(expression2)

print("\nExample 3")

def greeter(n): # n is called a PARAMETER, which is a placeholder for an ARGUMENT
    return f"Hi {n}!"

first = greeter("Arsen")
second = greeter("Ethan")
third = greeter("Shiven")

print(first, second, third)

print("\nExample 4")

def remainder(a, b):
    return a % b

result = remainder(3,2)
print(result)

print("\nExample 5")

def is_far(distance):
    # Insert base case
    if distance < 1:
        return "Error"
    
    if distance >= 100:
        return "That's far"
    elif distance <100 and distance >= 20:
        return "That's not too far"
    elif distance < 20 and distance >1:
        return "That's nearby"
    


print(is_far(-10))
print(is_far(200))
print(is_far(50))
print(is_far(5))    