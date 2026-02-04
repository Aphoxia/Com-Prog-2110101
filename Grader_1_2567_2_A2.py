Temp_s = float(input())
R_Temp = float(input())
time = float(input())
material = int(input())-1
windspeed = int(input())-1

windspeeds = [1.5,1,0.8]
materials = [0.05,0.02,0.01,0.015]

k = windspeeds[windspeed] * materials[material]
Temp_new = Temp_s
temp = 0
count = 0
while abs(Temp_new - temp) > 10**-3:
    temp = Temp_new
    Temp_new = Temp_new-(k*(Temp_new-R_Temp)*time)
    count += 1

print(count*time,round(Temp_new,3))


