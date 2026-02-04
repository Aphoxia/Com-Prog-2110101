
formula = input()
new_f = ""
for letter in formula:
    if letter in "-+":
        new_f += " "
    new_f += letter
total = 0
for number in new_f.split():
    total += int(number)
print(total)


