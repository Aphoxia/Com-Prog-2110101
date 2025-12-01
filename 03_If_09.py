import math
bd,bm,by,d,m,y = [int(e) for e in input().split(" ")]

overalldays = 0
# leap years happen when the year % 4 = 0 and year % 100 = 0 but ifs it year % = 0 | leap year
leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]
common_year = [31,28,31,30,31,30,31,31,30,31,30,31]

# Check leap or not for birth year
if (by % 4 == 0 and by % 100 != 0) or by % 400 == 0:  # Leap year
    overalldays += sum(leap_year[bm:]) + (leap_year[bm-1] - bd)
else: #common_year
    overalldays += sum(common_year[bm:]) + (common_year[bm-1] - bd)

# check leap year for right now
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    overalldays += sum(leap_year[:m-1]) + d
else: 
    overalldays += sum(common_year[:m-1]) + d

# lastly check middle part for exp 2015 - 2014 = 0 year in between or y - bm - 1
overalldays += 365 * (y-by-1)
# Test over all days
#print(overalldays)

#calculate factors
physical = math.sin( ( 2 * math.pi * overalldays ) / 23)
emotional = math.sin( ( 2 * math.pi * overalldays ) / 28)
intellectual = math.sin( ( 2 * math.pi * overalldays ) / 33)

#Print all statements 2 decimal points
print(f"{overalldays} {physical:.2f} {emotional:.2f} {intellectual:.2f}")

