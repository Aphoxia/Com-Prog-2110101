import math
a,b,c = input().split(",")
fixed_b = ("0" + b)[-len(b):]

fraction = int("9" * len(c) + "0" * len(b))
whole_num = (int(a) * fraction) + (int(fixed_b) * (fraction // (10 ** (len(b))))) +int(c)
# fixed b have 1 string but b have 0 string
divider = math.gcd(fraction,whole_num)
fraction //= divider
whole_num //= divider


print(f"{whole_num} / {fraction}")