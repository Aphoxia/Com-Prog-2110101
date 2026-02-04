def f1(a,b,c):
    min = max(a,b,c)
    if min > a and a > 0:
        min = a
    if min > b and b > 0:
        min = b
    if min > c and c > 0:
        min = c
    return min

def f2(a,b,c):
    max = min(a,b,c)
    if max < a and a < 0:
        max = a
    if max < b and b < 0:
        max = b
    if max < c and c < 0:
        max = c
    return max

def f3(a,b,c):
    number = abs(a + b + c)
    return str(number)[0]

def f4(a,b,c):
    number = abs(a + b + c)
    return str(number)[-1]

def main():
    s1,s2,a,b,c = [int(e) for e in input().split()]
    if s1 == 0 and s2 == 0:
        print(f1(a,b,c))
    elif s1 == 0 and s2 == 1:
        print(f2(a,b,c))
    elif s1 == 1 and s2 == 0:
        print(f3(a,b,c))
    elif s1 == 1 and s2 == 1:
        print(f4(a,b,c))
    else:
        print("Error")

exec(input().strip())
