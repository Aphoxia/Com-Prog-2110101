h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

t1 = h1 * 3600 + m1 * 60 + s1
t2 = h2 * 3600 + m2 * 60 + s2

time_different = ((86400 + (t2 - t1)) % 86400)

dh = time_different // 3600

time_different -= (dh * 3600)
dm = time_different // 60
time_different -= (dm * 60)
ds = time_different

print(f"{dh}:{dm}:{ds}")


