with open('Basics\File-Based-To-Do list.txt', 'w') as file:
    file.write('Learning Python!')

with open('Basics\File-Based-To-Do list.txt', 'a') as fileA:
    fileA.write('\nStep 1: Variables & Data Types: - Done')
    fileA.write('\n- int, float, str, bool.\n- Type conversion\n- type() function\n- Basic arithmetic')
    fileA.write('\nStep 2: Control Flow: - Done')
    fileA.write('\n- if, elif, else\n- Comparison operators\n- Logical operators\n- for loops\n- while loops\n- break, continue')
    fileA.write('\nStep 3: Data Structures: - Done')
    fileA.write('\n- Lists (indexing, slicing)\n- Tuples\n- Sets\n- Dictionaries\n- List comprehensions')
    fileA.write('\nStep 4: Functions: - Done')
    fileA.write('\n- Defining functions\n- Parameters & return values\n- Default arguments\n- Keyword arguments\n- Scope\n- Lambda functions')
    fileA.write('\nStep 5: Error Handling: - Done')
    fileA.write('\n- try, except\n- Multiple exceptions\n- finally\n- Raising exceptions')
    fileA.write('\nStep 6: File Handling: - Done')
    fileA.write('\n- open()\n- Read (r)\n- Write (w)\n- Append (a)\n- with statement')
with open('Basics\File-Based-To-Do list.txt', 'r') as fileR:
    content = fileR.read()
    print(content)
