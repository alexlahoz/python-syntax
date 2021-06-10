
#Example for a even generator with a function
def functionEven(limit):

    num = 1
    List = []

    while num < limit:
        List.append(num*2)
        num+=1

    return List

#print(evenGenerator(10))

############################################################

#Example for a even generator with a Generator
#The generator return a list therefore we don't need it
def generatorEven(limit):
    
    num = 1

    while num < limit:
        #yield return a iterable object
        yield num*2
        num+=1

devolveEvens = generatorEven(10)


print(next(devolveEvens))

print('Here can have more code')

print(next(devolveEvens))

""" for i in devolveEvens:
    print(i) """