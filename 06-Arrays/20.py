number = int(input('Number: '))

array = [15,38,7,23,14]
print(array)

def occurs(num, array):
    return True if num in array else False

if(occurs(number,array)):
    print(f'Result: number {number} appears in the array')
else:
    print(f'Result: number {number} does not appear in the array')