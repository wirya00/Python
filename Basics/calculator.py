def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: Division by zero")
    return a / b

def mod(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: Modulus by zero")
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
    
    while True:
        print('Type "exit" to exit')
        op = input("Insert operation (+, -, *, /, %): ")
        
        if op == "exit":
            break
        
        if op not in operations:
            print("Invalid operator")
            continue
        
        num1 = get_number("Insert first number: ")
        if num1 == "exit":
            break
        
        num2 = get_number("Insert second number: ")
        if num2 == "exit":
            break

        try:
            result = operations[op](num1, num2)
            print("Result:", result)
        except ZeroDivisionError as e:
            print(e)


if __name__ == "__main__":
    calculator()
