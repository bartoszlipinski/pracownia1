import re

with open('grades.txt') as f:
    txt = f.read()
    grades = re.findall('\d\.\d', txt)
    sum = 0
    for grade in grades:
        sum += float(grade)
    print(f'Mean: {sum / len(grades)}')
