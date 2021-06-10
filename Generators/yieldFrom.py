""" 
Cuando en python se usa "*" al inicio del parámetro quiere decir que va a recibir un número indeterminado de parámetros
Además le estamos indicando que esos argumentos los va a recibir en forma de tupla
"""

# def giveBackCities(*cities):
#     for element in cities:
#         for subElement in element:
#             yield subElement

# givenCities = giveBackCities('California','Texas','Florida','New Jersey',)

# print(next(givenCities))
# print(next(givenCities))
#Este código se puede ahorrar usando yiel from

def giveBackCities(*cities):
    for element in cities:
        #for subElement in element:
            yield from element

givenCities = giveBackCities('California','Texas','Florida','New Jersey',)

print(next(givenCities))
print(next(givenCities))