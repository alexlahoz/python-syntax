# Tuples cannot be modified
# Basic tuple
myTuple = ('Juan', True, 5)

# Printing all the tuple
print(myTuple[:])

# Converts the tuple in a list
myList = list(myTuple)

# Converts the list in a tuple
myTuple = tuple(myList)

# .count() returns how often the element is repeated in tuple
print(myTuple.count(5))

# len() returns how long the tuple is
print(len(myTuple))

# You can assign a tuple to a series of variables
name, boolean, age = myTuple
print(name, boolean, age)
