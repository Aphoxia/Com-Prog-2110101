
number_list = ["","A","B","C","D","E","F","G","H","I","J"]

code = input()
print(len(code))
a,b,c,d,e = code[3],code[10],code[17],code[24],code[31]
f,g,h,i,j = code[7],code[12],code[17],code[22],code[27]

first_pass = int(a + b + c + d + e)
second_pass = int(f + g +h + i + j)

Pass = str((first_pass + second_pass + 10000) % 10000 )
Pass = Pass[0:3]
character_list = [character for character in Pass]
word = int(character_list[0]) + int(character_list[1]) + int(character_list[2])
real_word = word % 10 + 1
Letter = number_list[real_word]

real_pass = Pass + str(Letter)
print(real_pass)




#92813912398100282033745980018127
#99999999999999999999999999999999
#00000000000000000000000000000000
