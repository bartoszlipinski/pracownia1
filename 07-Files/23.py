import csv

with open('students.txt') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    for row in reader:
        if int(row[2]) < 30:
            print(f'{row[0]} {row[1]} {row[4]}')
