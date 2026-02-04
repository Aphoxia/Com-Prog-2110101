a,b,c,d,e = [int(f) for f in input().split()]
if a >=e :
    i,n = 0,4
    while i <= n:
        if a >= b:
            a,b = b,a
        if b >= c:
            b,c = c,b
        if c >= d:
            c,d = d,c
        if d >= e:
            d,e = e,d
        i += 1
    print(a,b,c,d,e)
else:
    if a == 1:
        if b >= c:
            b,c = c,b
        if c >= d:
            c,d = d,c
        if d >= e:
            d,e = e,d
        if b <= c:
            if b <= d:
                print(round(((c+d)/2),2))
            else:
                print(round(((b+c)/2),2))
        else:
            if c<=d:
                print(round(((b+d)/2),2))
            else:
                print(round(((b+c)/2),2))
    else:
        ans = (((b**2)+(c**2)+(d**2))**(1/2)) / (a**2)
        print(round(ans,2))