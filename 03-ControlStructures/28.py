amountOfNumbers = 50
curr = 1
prev = 0
print('0 1 ', end="")
for i in range(amountOfNumbers-2):
    tmp = curr
    print(curr + prev, end=" ")
    curr = curr + prev
    prev = tmp


