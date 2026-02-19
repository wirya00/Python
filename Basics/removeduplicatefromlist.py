numbers = [1, 2, 2, 3, 1, 4, 4, 5, 6, 6, 6, 7, 7, 8, 8, 5]

i = 0

while i < len(numbers):

    j = i + 1

    while j < len(numbers):

        if numbers[j] == numbers[i]:
            del numbers[j]
        else:
            j = j + 1

    i = i + 1

print(numbers)

names = ["apple", "banana", "apple", "orange", "banana"]

i = 0

while i < len(names):

    print("\nOuter loop i =", i, "Value =", names[i])

    j = i + 1

    while j < len(names):

        print("   Comparing", names[i], "with", names[j])

        if names[j] == names[i]:
            print("   Duplicate found → deleting", names[j])
            del names[j]
            print("   List is now:", names)
        else:
            j = j + 1

    i = i + 1

print("\nFinal list:", names)
