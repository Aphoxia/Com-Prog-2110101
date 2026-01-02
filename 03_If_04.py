score = float(input())
match score:
    case num if num >= 80:
        print("A")
    case num if 80 > num >= 70:
        print("B")
    case num if 70 > num >= 60:
        print("C")
    case num if 60 > num >= 50: 
        print("D")
    case _:
        print("F")


    
    

