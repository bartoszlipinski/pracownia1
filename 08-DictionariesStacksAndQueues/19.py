import math

els = []
operators = ['+', "-", '*', "/"]

print('Enter RPN equation: ')
while True:
    userinput = input()
    if userinput == "=":
        els.append(userinput)
        break
    elif userinput in operators:
        els.append(userinput)
    else:
        els.append(int(userinput))

stack = []
for el in els:
    if type(el) is int:
        stack.append(el)
    elif el in operators:
        i2 = stack.pop()
        i1 = stack.pop()
        if el == "+":
            stack.append(i1+i2)
        elif el == "-":
            stack.append(i1-i2)
        elif el == "*":
            stack.append(i1*i2)
        else:
            stack.append(i1/i2)
    else:
        val = stack.pop()
        print(f'Result: {val}')