#LIST
numbers = [10, 20, 30, 40, 50]
first_item = numbers[0]
second_item = numbers[1]
last_item = numbers[-1]

print('Numbers:', numbers)

print(first_item, second_item, last_item)

part = numbers[1:4]

print('Part 1:4 of numbers:', part)
print('Slice :3 of numbers:', numbers[:3])
print('Slice 2: of numbers:', numbers[2:])
print('Copy of numbers by slicing ":" :', numbers[:])

#TUPLES
coordinates = (345, 123)
x = coordinates[0]
y = coordinates[1]

print('X = ', x)
print('Y = ', y)

#SETS
my_sets = {1, 2, 3, 4}

print('my_sets:', my_sets)

sets_input = input('What number do you want to put inside my_sets?')
my_sets.add(sets_input)

print('Updated my_sets:', my_sets)

#DICTIONARIES
promo = {}
not_promo = {}

name_input = input('Whats your name?')
promo_input = input('Do you want to be notfied for promo? y/n')

if promo_input == 'y':
    promo['Name'] = name_input
    promo['Promo'] = promo_input
else:
    not_promo['Name'] = name_input
    not_promo['Promo'] = promo_input

print('Promo list:', promo)
print('Non-Promo list:', not_promo)