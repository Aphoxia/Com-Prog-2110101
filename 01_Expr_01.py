import math
number = int(input())
lower_limit = math.pow(2*math.pi , 1/2) * math.pow(number,number + 0.5) * math.pow(math.e , -number + ( 1/ ((12 * number) + 1)))
Upper_limit = math.pow(2*math.pi , 1/2) * math.pow(number,number + 0.5) * math.pow(math.e , -number + ( 1/ ((12 * number))))
print(lower_limit , Upper_limit)
