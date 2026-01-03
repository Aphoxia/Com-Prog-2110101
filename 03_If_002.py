thrity_first = [1,3,5,7,8,10,12]
thirty = [4,6,9,11]


d,m,y = [int(e) for e in input().split()]
y -= 543
n = 31
if m in thirty:
    n = 30
else:
    if m == 2:
        n = 28
        if y % 400 == 0:
            n = 29
        if (y % 4 == 0) and (y % 100 != 0):
            n = 29
d += 15
if d > n:
    d -= n
    m += 1
if m > 12:
    m -= 12
    y += 1
y += 543
print(f'{d}/{m}/{y}')
