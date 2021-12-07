file1 = open('countries.txt')

file2 = open('copylines.txt', 'w')

for line in file1:
    file2.write(line)

file2.close()

file1.close()
