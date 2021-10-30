firstNumber = int(input('Enter first number: '))
secondNumber = int(input('Enter second number: '))

array = [firstNumber, secondNumber]
array.sort()

print(f'Numbers in ascending order: {array[0]}, {array[1]}')
