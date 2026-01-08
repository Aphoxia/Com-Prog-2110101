number = int(input())
decimal = len(str(number))
if decimal >= 4 and decimal< 7:
    number /= 1000
    if number > 10:
        print(f"{number:.0f}K")
    else:
        print(f"{number:.1f}K")
elif decimal >= 7 and decimal < 11:
    number /= 1000000
    if number > 10:
        print(f"{number:.0f}M")
    else:
        print(f"{number:.1f}M")
elif decimal >= 11:
    number /= 1000000000
    if number > 10:
        print(f"{number:.0f}B")
    else:
        print(f"{number:.1f}B")