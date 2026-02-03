lines = int(input())
index = []
for line in range(0,lines):
    x = [e for e in input().strip().split()]
    if lines % 2 == 0:
        if line % 2 == 1:
            index += x[::-1]
        else:
            index += x
    else:
        if line % 2 == 1:
            index += x
        else:
            index += x[::-1]

index =["."] + index[::-1]
print(index)
number = 0
dice_roll = [int(roll) for roll in input().strip().split()]

output = ""
for dice in dice_roll:
    number += dice
    if number >= len(index)-1:
        output += "win"
        break
    elif index[number] != ".":
        number = int(index[number][1:])
        output += f'{number} '
    else:
        output += f'{number} '

print(output)


