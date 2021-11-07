import mymath

game = True
randNumber = mymath.generate_number()

while game:
    if randNumber == mymath.read_number():
        game = False
        print('You win!')