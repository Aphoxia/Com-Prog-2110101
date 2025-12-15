import math
x = float(input())
y = float(input())
Mosteller = math.sqrt( x * y ) / 60
Haycock = 0.024265 * ( x ** 0.5378 ) * ( y ** 0.3964 )
Boyd = 0.0333 * (x ** (0.6157 - (0.0188 * math.log10(x))) * ( y ** 0.3 ))
print(f"""{Mosteller}
{Haycock}
{Boyd}""")