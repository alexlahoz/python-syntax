
names = {
    'John':5,
    'Richard':10,
    'Mark':15
}


def test(nameList):
    for e in nameList:
        for subE in e:
            print(subE)

test(names)

print(names)