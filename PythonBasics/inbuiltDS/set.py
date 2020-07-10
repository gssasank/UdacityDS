# mutable and unorderd, no duplicates
numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)

fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element
print(fruit)

#U N O R D E R E D

# BOTH SETS AND DICTIONARIES ARE INITIALIZED WITH {}

#* You can use curly braces to define a set like this: {1, 2, 3}.
#  However, if you leave the curly braces empty like this: {} Python will instead create an empty dictionary.
#  So to create an empty set, use set().