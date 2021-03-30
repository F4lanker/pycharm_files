import re

n, m = [int(i) for i in input().split()]
field = []  # Заводим поле
res = []  # Итоговое поле сапера


def ranger(x, y):
    """ Функция проверяет входит ли запрашиваемая точка в диапазон  и не является ли элемент миной"""
    if x < 0 or y < 0:
        return False
    elif x >= n or y >= m:
        return False
    elif res[x][y] == '*':
        return False
    else:
        return True


def mine(x, y):
    """ Функция находит все соседние клетки с миной, и добавляет к ним +=1"""
    if ranger(x - 1, y - 1) is True:
        res[x - 1][y - 1] += 1

    if ranger(x, y - 1) is True:
        res[x][y - 1] += 1

    if ranger(x + 1, y + 1) is True:
        res[x + 1][y + 1] += 1

    if ranger(x - 1, y) is True:
        res[x - 1][y] += 1

    if ranger(x + 1, y) is True:
        res[x + 1][y] += 1

    if ranger(x - 1, y + 1) is True:
        res[x - 1][y + 1] += 1

    if ranger(x, y + 1) is True:
        res[x][y + 1] += 1

    if ranger(x + 1, y - 1) is True:
        res[x + 1][y - 1] += 1


for i in range(n):
    field.append(re.findall(r'.', input()))  # заводим поле и разбиваем его на символы регуляркой
    res.append([0] * m)  # поле с резубьтатами заполняем нулями
for i in range(n):
    for j in range(m):  # перебираем элементы поля по одному
        current = field[i][j]
        if current == '*':
            res[i][j] = '*'
            mine(i, j)
for row in res:
    print(' '.join([str(elem) for elem in row]))

# input sample:
#4 4
#..*.
#**..
#..*.
#....