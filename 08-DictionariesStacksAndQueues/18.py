num = int(input('Natural number: '))
stack = []
binary = ''
while num > 0:
    stack.append(num % 2)
    num = num // 2
for i in range(len(stack)):
    binary += str(stack.pop())
print(f'Binary number: {binary}')