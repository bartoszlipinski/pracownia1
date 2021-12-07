with open('shoppinglist.txt', 'w') as f:
    with open('MeatAndFish.txt') as f2:
        f.write(f'{f2.read()}\n')
    with open('GrainsAndBread.txt') as f3:
        f.write(f3.read())
