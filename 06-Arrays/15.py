colors = ['red', 'blue', 'green', 'cyan', 'magenta', 'yellow', 'black']

f = open('15.txt', 'w')
for i in colors:
    f.write(f'{i}\n')
f.close()

f = open('15.txt', 'r')
print(f.read())
