phone_num = input()

if len(phone_num) == 10:
    if phone_num[0:2] == "06" or phone_num[0:2] == "08" or phone_num[0:2] == "09":
        print("Mobile number")
    else:
        print("Not a mobile number")
else:
    print("Not a mobile number")