#funcs without name which can be used once in the code
#useful with functions which take in other functions as values
multiply = lambda x, y: x * y
print(multiply(4, 7))

#Q1

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]


mean = lambda num_list : sum(num_list) / len(num_list)
averages = list(map(mean, numbers))
print(averages)

"""map() is a higher-order built-in function that takes a function and iterable as inputs, 
and returns an iterator that applies the function to each element of the iterable. 
The code above uses map() to find the mean of each list in numbers to create the list averages.
 Give it a test run to see what happens.
Rewrite this code to be more concise by replacing the mean function with a lambda expression defined within the call to map()."""

#Q2

"""filter() is a higher-order built-in function that takes a function and iterable as inputs and 
    returns an iterator with the elements from the iterable for which the function returns True.
    The code below uses filter() to get the names in cities that are fewer than 10 characters long to create the list short_cities.
     Give it a test run to see what happens.

    Rewrite this code to be more concise by replacing the is_short function with a lambda expression defined within the call to filter()."""


cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]


#is_short = lambda name : len(name) < 10 OR 'below'
short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)








