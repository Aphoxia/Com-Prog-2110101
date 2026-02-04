def get_copies (text,pattern):
    check_copies = len(text)//len(pattern)
    while check_copies > 1:
        if pattern * check_copies in text:
            return check_copies
        check_copies -= 1
    return 0

pattern = input()
lines = int(input())
for _ in range(0,lines):
    text = input()
    copies = get_copies(text,pattern)
    print(copies)

