leadingNumbers = int(input('Enter amount of numbers: '))

print(f'Range: {leadingNumbers}')
print('Prime numbers: ', end="")
i = 1
primes = 0
while primes < leadingNumbers:
    factors = 0
    for j in range(1, i + 1):
        if i % j == 0:
            factors += 1
    if factors == 2:
        print(i, end=" ")
        primes += 1
    i += 1
