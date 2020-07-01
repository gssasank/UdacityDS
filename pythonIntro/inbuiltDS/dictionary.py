elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary

print("carbon" in elements)
print(elements.get("dilithium")) # this is better because it reurns None, not an error
print(elements)
n = elements.get("dilithium")
print(n is None)
print(n is not None)

#Dictionary keys must be immutable, that is, lists cannot be used as keys
# 
#Dictionaries have a related method that's also useful, get(). get() looks up values in a dictionary,
#but unlike looking up values with square brackets, get() returns None (or a default value of your choice) if the key isn't found. 
# If you expect lookups to sometimes fail, get() might be a better tool than normal square bracket lookups.

#U N O R D E R E D

# A dictionary itself is mutable, but each of its individual keys must be immutable.