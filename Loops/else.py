
email = input('Type your email: ')

for i in email:

    if i == '@':
        
        at = True

        #break the code and continue for
        break;

#this else is part of for
else:
    at = False

print(at)
