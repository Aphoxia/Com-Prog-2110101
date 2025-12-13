import math
def upper():
    a = math.pi - (math.factorial(10) / pow(8,8)) + (pow(math.log(9.7), 7/math.sqrt(7) - math.sin(math.radians(40))))
    return a

def lower():
    b = pow(1.2,pow(2.3,3))
    return b

print( upper() / lower())