array = [15,8,31,47,2,19]

print("initial array:", end=" ")
for i in array:
    print(i, end=" ")
print(f"\nreverse array:", end=" ")
for i in range(1, len(array) + 1):
    print(array[len(array) - i], end=" ")
