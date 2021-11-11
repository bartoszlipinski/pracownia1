def sumOfDigits(n):
    numbers = str(n)
    sum = 0
    for i in numbers:
        sum += int(i)
    return sum

print(sumOfDigits(7182))