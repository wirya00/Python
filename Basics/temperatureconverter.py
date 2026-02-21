def ftoc(f):
    c = (f - 32) / (9/5)
    print(f,'Fahrenheit =', c, 'Celsius')
    print('------------------------------')
    return c

def ctof(c):
    f = (c * (9 / 5)) + 32
    print(c, 'Celsius =', f, 'Fahrenheit')
    print('------------------------------')
    return f

def tempConvert():
    print('Welcome to my temperature converter.')
    while True:
        print('"exit" to exit')
        print('"C" to convert Celsius to Fahrenheit')
        print('"F" to convert Fahrenheit to Celsius')
        choice = input('Enter your choice: ')
        if choice.lower() == 'exit':
            break
        numbers = input('Enter the degree; Only numbers: ')
        if numbers.lower() == 'exit':
            break
        numbers = float(numbers)

        if choice.lower() == 'f':
            ftoc(numbers)
        elif choice.lower() == 'c':
            ctof(numbers)
        else:
            print('Invalid choice.')
            continue

tempConvert()
