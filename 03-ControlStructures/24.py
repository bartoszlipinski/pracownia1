maxWidth = 5

for i in range(1, maxWidth*2):
    if i <= maxWidth:
        print(i*"*")
    else:
        print((maxWidth-(i-maxWidth))*"*")
