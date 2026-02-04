Flush = ["CCCCC","HHHHHH","DDDDD","SSSSS"]
Straight = "AKQJX98765432A"
R_Straight_Flush = "AKQJX"

lines = int(input())
for _ in range(0,lines):
    poker = input().strip("|")
    Is_Flush = poker[1::3] in Flush
    Is_Straight = poker[::3] in Straight
    Is_R_Straight = poker[::3] in R_Straight_Flush

    if Is_R_Straight and Is_Flush:
        print("Royal Stright Flush")
    elif Is_Straight and Is_Flush:
        print('Straight Flush')
    elif Is_Flush:
        print("Flush")
    elif Is_Straight:
        print('Straight')
    else:
        print("None")

        
                
              
