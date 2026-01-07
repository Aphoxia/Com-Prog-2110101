Code = input()
last_digit = (11-(13*int(Code[0])+12*int(Code[1])+11*int(Code[2])+10*int(Code[3])+9*int(Code[4])+8*int(Code[5])+7*int(Code[6])+6*int(Code[7])+5*int(Code[8])+4*int(Code[9])+3*int(Code[10])+2*int(Code[11])) % 11) % 10
print(f'{Code[0]} {Code[1:5]} {Code[5:10]} {Code[10:12]} {last_digit}')

#123456789012
#310030011214
#110070234512