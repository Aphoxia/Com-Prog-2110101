first_nomanine = input().split()
second_nomanine = input().split()

Grade = ["F","D","C","B","A"]

if first_nomanine[2] == "A" and second_nomanine[2] == "A":
    if float(first_nomanine[1]) > float(second_nomanine[1]):
        print(first_nomanine[0])
    elif float(first_nomanine[1]) < float(second_nomanine[1]):
        print(second_nomanine[0])
    else:
        if Grade.index(first_nomanine[3]) > Grade.index(second_nomanine[3]):
            print(first_nomanine[0])
        elif Grade.index(first_nomanine[3]) < Grade.index(second_nomanine[3]):
            print(second_nomanine[0])
        else:
            if Grade.index(first_nomanine[4]) > Grade.index(second_nomanine[4]):
                print(first_nomanine[0])
            elif Grade.index(first_nomanine[4]) < Grade.index(second_nomanine[4]):
                print(second_nomanine[0])
            else:
                print("Both")
elif first_nomanine[2] == "A" and second_nomanine[2] != "A":
    print(first_nomanine[0])

elif first_nomanine[2] != "A" and second_nomanine[2] == "A":
    print(second_nomanine[0])

else:
    print("None")