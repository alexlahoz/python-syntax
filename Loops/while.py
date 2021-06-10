i = 1

while i <= 10:
    print('Exec', i)
    i = i+1    

print('End')


number = int(input('Type a positive number: '))

while number < 0:
    print('Your are typed a negative number try again')
    number = int(input('Type a positive number: '))