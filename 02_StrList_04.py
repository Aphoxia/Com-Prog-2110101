M = input()
N = int(input())

number_string =("0" * N ) + M
index = max(N,len(M))

print(number_string[-index:])