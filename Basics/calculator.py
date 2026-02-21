def add(a, b):
    result = a + b
    return result

def sub(a, b):
    result = a - b
    return result

def mul(a, b):
    result = a * b
    return result

def div(a, b):
    if a == 0:
        return False
    if b == 0:
        return False
    result = a / b
    return result

def mod(a, b):
    result = a % b
    return result



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

        num2 = input('Please insert your second number: ')
        if num2.lower() == 'exit':
            break

        num2 = float(num2)

        if op == '+':
            result = add(num1, num2)
            print(result)
        elif op == '-':
            result = sub(num1, num2)
            print(result)
        elif op == '*':
            result = mul(num1, num2)
            print(result)
        elif op == '/':
            result = div(num1, num2)
            print(result)
        elif op == '%':
            result = mod(num1, num2)
            print(result)
        else:
            print('Invalid operator')
            continue

calculator()
