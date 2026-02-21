def isPrime(numbers):
    if numbers <= 1:
        return False
    
    i = 2

    while i < numbers:
        if numbers % i == 0:
            return False
        i = i + 1

    return True

def main():
    while True:
        print('Type "exit" to exit')
        choice = input('Numbers you want to check: ')
        if choice.lower() == 'exit':
            break
        choice = int(choice)
        if isPrime(choice) == False:
            print(choice, 'is Not a prime number.')
        else:
            print(choice, 'is a Prime number.')

main()