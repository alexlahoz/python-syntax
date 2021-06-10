
# Basic lists
myList = [1, True, 'Juan', 'Manuel', 6]

# The : is used to print all elements of the list
print(myList[:])

# You can also pass the required item index
print(myList[0])

# And you can also pass negative numbers, but the first index is not 0 and start from end of the list
print(myList[-2])

# All the elements until the last indicated
print(myList[0:3])

# .append() is used to add new elements in the end of the list
myList.append('Imanol')

# .insert() is used to add new elements to the index you want from the list
# .insert() need two parameters, index and element.
myList.insert(2, 'Carlos')

# .extend() is used to add some elements in the end of the list
myList.extend(['Pedro', 'Mateo', False, 5])

# .index is used to return the place of element in list
print(myList.index('Juan'))

# in is used to return True or False if the first parameter is in the list
print('Juan' in myList)

# .remove() is used for remove the element passed to the parameter
myList.remove('Juan')

# .pop() is used for remove last element
myList.pop()

# * 3 repeat the list the times you multiply
myList2 = [1, 2, 3] * 3
