from random import randint

with open('randomintegers.txt', 'w') as f:
    for i in range(50):
        f.write(f'{randint(100, 999)}\n')
