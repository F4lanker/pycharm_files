x, y = [int (i) for i in (input()).split('/')]
result = []
result.append(x//y)
rest = x%y
while rest != 1/y or rest == 0:
    rest = (x%y)/y
    if x%y