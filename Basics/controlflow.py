import random

#Ask the user to input a number to check
number = int(input('Input a number to check;Odd or even:'))

# % = The leftover of a divition. So 2 % 2 is 0, 4 % 2 is 0, 3 % 2 is 1;
if number % 2 == 0:
    print('Even')
else:
    print('Odd')

number_guessed = False
guess_number = random.randint(1, 100)

while number_guessed == False:
    guess = int(input('Guess a number:'))
    if guess == guess_number:
        number_guessed = True
        print('You are correct! The number was:', guess_number)
        break
    elif guess < guess_number:
        print('Higher')
    elif guess > guess_number:
        print('Lower')

number_input = int(input('What number do you want to multiply:'))
for i in range(1, 11):
    result = number_input * i
    print(number_input, 'X', i, '=', result)