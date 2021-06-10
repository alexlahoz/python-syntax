#Basic dictionary
myDictionary = {'España':'Madrid', 'Francia':'París'}

print(myDictionary['Francia'])
print(myDictionary)

#Add new element to the end of the dictionary
myDictionary['Italia'] = 'Roma'

print(myDictionary)

#del removes the indicated element
del myDictionary['Italia']

#You can use the values of a tuple in a dictionary
myTuple = ('España', 'Francia')
mySecondDictionary = {myTuple[0]:'Madrid', myTuple[1]:'París'}
print(mySecondDictionary)

#You can use tuples inside the dictionary
myThirdDictionary = {23:'Jordan', 'Nombre':'Michael', 'Equipo':'Chicago','Anillos':[1991,1992,1993,1996,1997,1998]}
print(myThirdDictionary['Anillos'])

#You can use dictionaries inside the dictionaries
myFourthDictionary = {23:'Jordan', 'Nombre':'Michael', 'Equipo':'Chicago','Anillos':{'Temporadas':[1991,1992,1993,1996,1997,1998]}}

#Methods

#.keys return the keys of dictionary
print(myDictionary.keys())

#.values return the values of dictionary
print(myDictionary.values())

#.values return how keys have the dictionary
print(len(myDictionary))
