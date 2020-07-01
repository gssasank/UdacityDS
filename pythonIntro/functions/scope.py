egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()

#In the last video, you saw that within a function, we can print a global variable's value successfully without an error. 
# This worked because we were simply accessing the value of the variable. 
# If we try to change or reassign this global variable, however, as we do in this code, we get an error. 
# Python doesn't allow functions to modify variables that aren't in the function's scope.

