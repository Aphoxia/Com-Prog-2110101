import math
a = float(input())
b = float(input())
c = float(input())

x1 = round((-b - math.sqrt((b**2) - (4*a*c))) / (2*a) , 3)
x2 = round((-b + math.sqrt((b**2) - (4*a*c))) / (2*a) , 3)

print(x1 , x2 )
#print(f"{x1:.3f} {x2:.3f}")