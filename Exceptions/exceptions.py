def divide():

    try:
        n1 = float(input("Type the first number: "))
        n2 = float(input("Type the second number: "))

        print('The division are: ', n1 / n2 )

    except ValueError:
        print('The value typed are incorrect')

    except ZeroDivisionError:
        print('Cannot divides by 0')

    except:
        print('General error has captured')

    #The finally alwais execute
    finally:
        print('Finished calculation')

    print('Continue the program')

divide()