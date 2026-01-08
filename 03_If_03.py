Numbers = [float(n) for n in input().split()]

max_number = Numbers[0]
min_number = Numbers[0]
for number in Numbers:
    if max_number > number:
        max_number= number

for number in Numbers:
    if min_number < number:
        min_number = number

Numbers.remove(max_number)
Numbers.remove(min_number)

result = 0
for number in Numbers:
    result += number
result /= len(Numbers)
print(round(result,2))
