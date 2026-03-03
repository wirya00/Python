from datetime import datetime

def write_log(message):
    timestamp = datetime.now().strftime('[%d-%m-%Y %H:%M:%S]')
    with open('Python Basics\Log.log', 'a') as file:
        file.write(f'{timestamp} {message}\n')

def add(a, b):
    write_log('Add: User used the add function and succeded.')
    return a + b

def sub(a, b):
    write_log('Sub: User used the sub function and succeded.')
    return a - b

def mul(a, b):
    write_log('Mul: User used the mul function and succeded.')
    return a * b

def div(a, b):
    if b == 0:
        write_log('Error: Division by zero')
        raise ZeroDivisionError("Error: Division by zero")
    write_log('Div: User used the div function and succeded.')
    return a / b

def mod(a, b):
    if b == 0:
        write_log('Error: Modulus by zero')
        raise ZeroDivisionError("Error: Modulus by zero")
    write_log('Mod: User used the mod function and succeded.')
    return a % b


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "%": mod
}


def get_number(prompt):
    while True:
        value = input(prompt)
        if value.lower() == "exit":
            return "exit"
        try:
            return float(value)
        except ValueError:
            print("Only numbers.")


def calculator():
    print("Welcome to my Calculator.")
    write_log('Starting the calculator...')

    loop_Number = 0

    while True:
        loop_Number = loop_Number + 1
        write_log(f'This is the {loop_Number} times user use the calculator.')

        print('Type "exit" to exit')
        op = input("Insert operation (+, -, *, /, %): ")
        
        if op == "exit":
            write_log('User is exiting the program.')
            break
        
        if op not in operations:
            write_log('User tried to input an invalid operator.')
            print("Invalid operator")
            continue
        
        num1 = get_number("Insert first number: ")
        if num1 == "exit":
            write_log('User is exiting the program.')
            break
        
        num2 = get_number("Insert second number: ")
        if num2 == "exit":
            write_log('User is exiting the program.')
            break

        try:
            write_log('User succeded inputting correct operation, first number, and the second number. Proceeding...')
            result = operations[op](num1, num2)
            print("Result:", result)
        except ZeroDivisionError as e:
            print(e)
        finally:
            print('Thank you for using my calculator.')


if __name__ == "__main__":
    calculator()
