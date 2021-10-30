array = []

while True:
    num = int(input('Enter number: '))
    if(num == 0):
        break
    array.append(num)

q = len(array)
s = 0
for i in range(q):
    s += array[i]
m = s/q

print(f'RESULT: Quantity = {q}, Sum = {s}, Mean = {round(m)}')
