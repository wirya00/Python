def add(a, b):
    result = a + b
    print(result)

def sub(a, b):
    result = a - b
    print(result)

def mul(a, b):
    result = a * b
    print(result)

def div(a, b):
    result = a / b
    print(result)

def mod(a, b):
    result = a % b
    print(result)



print('Welcome to my Calculator.')
def calculator():
    while True:
        print('Type "exit" to exit')
        op = input('Please insert your operation (+, -, *, /, %): ')
        if op == 'exit':
            break
        num1 = input('Please insert your first number: ')
        if num1.lower() == 'exit':
            break

        num1 = float(num1)

        num2 = input('Please inser your second number: ')
        if num2.lower() == 'exit':
            break

        num2 = float(num2)

        if op == '+':
            add(num1, num2)
        elif op == '-':
            sub(num1, num2)
        elif op == '*':
            mul(num1, num2)
        elif op == '/':
            div(num1, num2)
        elif op == '%':
            mod(num1, num2)
        else:
            print('Invalid operator')
            continue

calculator()
