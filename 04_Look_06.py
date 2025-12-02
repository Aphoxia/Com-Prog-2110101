n = int(input())

# print the first line
for i in range (n):
    if i == (0 or 1):
        print("." * (n - i) + "*")
    elif i > 1:
        print("." * (n - i) + "*" + "." * (2 *  (i - 1) - 1) + "*")


# print base line
print( "*" * (2 * n - 1))