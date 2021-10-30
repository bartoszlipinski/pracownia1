noOfTries = 0
key = "0805"
locked = True

while locked:
    if noOfTries == 3:
        print('Sorry, your payment card has been blocked.')
        break
    code = input('Enter the PIN code: ')
    if code == key:
        locked = False
        print('You entered correct PIN code')
    else:
        noOfTries += 1
        print('Incorrect...')
