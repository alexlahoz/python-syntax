def sum(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        print('Cannot divides by 0')
        return 'The operation has failed'

while True:

    try:
        n1 = int(input('Type the first number: '))
        n2 = int(input('Type the second number: '))
        break
    except ValueError:
        print('You must type a integer value. Try again')


operation = input(
    'Type the number of the favorite operation \n 1.- Sum \n 2.- Subtract \n 3.- Multiply \n 4.- Divide \n Option: ' 
)


if operation == "1":
    print(sum(n1, n2))

elif operation == "2":
    print(subtract(n1, n2))

elif operation == "3":
    print(multiply(n1, n2))

elif operation == "4":
    print(divide(n1, n2))

else:
    print('An error has ocurred')


print('The program continue...')
    
      