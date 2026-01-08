weight = int(input().strip())
match weight:
    case n if n < 100:
        print("18")
    case n if 250 > n > 100:
        print("22")
    case n if 500 > n > 250:
        print("28")
    case n if 1000 > n > 500:
        print("38")
    case n if 2000 > n > 1000:
        print("58")
    case _:
        print("Reject")