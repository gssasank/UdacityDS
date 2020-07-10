cast = {
           "Jerry Seinfeld": [1,2],
           "Julia Louis-Dreyfus": [3,4],
           "Jason Alexander": [5,6],
           "Michael Richards": [7,8]
       }

print("Iterating through keys:")
for key in cast:
    print(key)

print("\nIterating through keys and values:")
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))
    
# items is an awesome method that returns tuples of key, value pairs, which you can use to iterate over dictionaries in for loops.
# this tuple will be like [("Jerry Seinfeld",[1,2]),.....]
# the above is a list of tuples whose items may not be in order always.....