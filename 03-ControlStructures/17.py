x = 4
y = -5

if y == 0 and x != 0:
    print(f'Point P({x},{y}) is on x axis')
elif x == 0 and y != 0:
    print(f'Point P({x},{y}) is on y axis')
elif x == 0 and y == 0:
    print(f'Point is located in position (0,0)')
elif x > 0:
    if y > 0:
        print(f'Point P({x},{y}) is in first quadrant of the coordinate system')
    else:
        print(f'Point P({x},{y}) is in fourth quadrant of the coordinate system')
else:
    if y > 0:
        print(f'Point P({x},{y}) is in second quadrant of the coordinate system')
    else:
        print(f'Point P({x},{y}) is in third quadrant of the coordinate system')