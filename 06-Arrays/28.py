array = [1111, 223, 5, 3, 1, 17, 4, 906]

length = len(array) * 5 + 1

for i in range(3):
    if i != 1:
        print(length * '-')
    else:
        print('|', end="")
        for j in range(len(array)):
            if array[j] < 10:
                print(f'   {array[j]}|', end="")
            elif array[j] < 100:
                print(f'  {array[j]}|', end="")
            elif array[j] < 1000:
                print(f' {array[j]}|', end="")
            else:
                print(f'{array[j]}|', end="")

        if j == len(array) - 1:
            print()
