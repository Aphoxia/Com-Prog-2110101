Decrypt_Mess = input()
first_number = int(Decrypt_Mess[3::7])
second_number = int(Decrypt_Mess[7::5])

result = str(first_number + second_number + 10000)
third_number = result[-4:-1]
second_result = int(third_number[0]) + int(third_number[1]) + int(third_number[2])
fourth_number = int(str(second_result)[-1:]) + 1


Code = "_ABCDEFGHIJK"
letter = Code[fourth_number]

print(third_number + letter)