file1 = open('countries.txt')

file2 = open('copy.txt', 'w')

file2.write(file1.read())

file2.close()

file1.close()
