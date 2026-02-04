date,money,t_month,s_month = [e for e in input().split()]
d,m,y = date.split("/")

money = int(money)
for i in range(1,int(t_month)+1):
    interest = 0
    if (i+int(s_month)-1 )%12 == int(m)%12:
        interest += 1
    match i:
        case i if i % 4 == 1:
            interest += 1
        case i if i % 4 == 2:
            interest += 2
        case i if i % 4 == 3:
            interest += 3
        case i if i % 4 == 0:
            interest += 4
    money_gain = money * (interest/100) / 12

    money += money_gain
    

print(round(money,2))
