a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b) # is equal or not
print(a is b) # is identical or not
print(a == c)
print(a is c)

# List a and list b are equal and identical. List c is equal to a (and b for that matter) since they have the same contents. 
# But a and c (and b for that matter, again) point to two different objects, i.e.,
#  they aren't identical objects. That is the difference between checking for equality vs. identity.