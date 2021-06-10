# Basic example of continue
for i in 'python':

    #if this condition is true continue ignore this loop back and don`t print 'h'
    if i == 'h':
        continue
    print(i)


######################################################

name = 'ale x'
accountant = 0

#"accountant+=1" is same of "accountant = accountant + 1"
for i in name:

    #this ignore the white space
    if i == ' ':
        continue
    accountant+=1
    print(accountant)