text = input()
max_char = text[0]
max_char_count = 1

count = 1
char = text[0]
for i in range(0,len(text)):
    if text[i] == char:
        count += 1
    else:
        if count > max_char_count:
            max_char_count = count
            max_char = char
            
        char = text[i]

        count = 1

if count > max_char_count:
    max_char_count = count
    max_char = char
print(max_char,max_char_count)



