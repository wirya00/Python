import csv

with open('Basics\csvfile.csv', 'r') as file1:
    csvFile1 = csv.DictReader(file1) #DictReader() makes the csv to be a dictionary

    for row in csvFile1:
        print(row)


with open('Basics\csvfile.csv', 'r') as file2:
    csvFile2 = csv.reader(file2) #reader() makes the csv to be a list

    #Skips header with next() built-in function
    next(csvFile2)

    for row in csvFile2:
        print(row)

with open('Basics\csvfile.csv', 'r') as file3:
    csvFile3 = csv.DictReader(file3)

    for row in csvFile3:
        print(f'ID: {row['id']}')
        print(f'Name: {row['name']}')
        print(f'Age: {row['age']}')
        print(f'City: {row['city']}')
        print(f'Score: {row['score']}')

with open('Basics\csvfile.csv', 'r') as file4:
    csvFile4 = csv.reader(file4)

    for row in csvFile4:
        print(row)
