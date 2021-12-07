name = input('Filename: ')
try:
    with open(name) as f:
        lines = 0
        for line in f:
            lines += 1
        print(f'Number of lines: {lines}')
except:
    print('File does not exist')
