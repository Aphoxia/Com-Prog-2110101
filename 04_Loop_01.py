numbers_list = []
while True:
    number = input()
    if number == "q":
        break
    else:
        numbers_list.append(float(number))
sum = 0
if len(numbers_list) != 0:
    for n in numbers_list:
      sum += n
    final = sum / len(numbers_list)
    print(round(final,2))
else:
    print("No data")

    