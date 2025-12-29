def str2hms(hms_str):
    t = hms_str.split(":")
    return int(t[0]),int(t[1]),int(t[2])

def hms2str(h,m,s):
    return (('0' + str(h))[-2:]) +":"+ (('0' + str(m))[-2:]) +":" + (('0' + str(s))[-2:])

def to_sec(h,m,s):
    second = h * 3600 + m * 60 + s
    return second

def to_hms(sec):
    h = sec // 3600
    sec %= 3600
    m = sec // 60
    sec %= 60
    s = sec
    return h,m,s

def diff(h1,m1,s1,h2,m2,s2):
    time1 = to_sec(h1,m1,s1)
    time2 = to_sec(h2,m2,s2)
    dt = time2 - time1
    dh,hm,ds = to_hms(dt)
    return dh,hm,ds


def main():
    hms_start = (input())
    hms_stop = (input())
    h1,m1,s1 = str2hms(hms_start)
    h2,m2,s2 = str2hms(hms_stop)
    dh,dm,ds = diff(h1,m1,s1,h2,m2,s2)
    total_time_diff = hms2str(dh,dm,ds)
    print(total_time_diff)

    
exec(input())