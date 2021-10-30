amount = int(input('Enter the amount in PLN: '))
coin5 = 0
coin2 = 0
coin1 = 0
print(f'The amount of PLN {amount} in coins:')
while amount > 0:
    if amount > 5:
        coin5 += 1
        amount -= 5
    elif amount > 2:
        coin2 += 1
        amount -= 2
    else:
        coin1 += 1
        amount -= 1
print(f'5 zł - {coin5}\n2 zł - {coin2}\n1 zł - {coin1}')
