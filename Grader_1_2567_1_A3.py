lines = int(input())
full_str = ""
for line in range (0,lines):
    text = input()
    lenght = len(text)
    
    full_str += text
cmd = input()
if cmd == "rot180":
    full_str = full_str[::-1]
    for i in range (0,lines):
        print(full_str[(lenght*i):(lenght*(i+1))])

if cmd == "rot90":
    for i in range(0,lenght):
        print(full_str[i::lenght][::-1])

