with open('sample3.txt') as f:
    line = 0
    for l in f:
        if line % 5 == 0 and line != 0:
            input('Press enter to continue...')
        print(l)

        line += 1
