def sqrt_n_times ( x,n ):
    return x ** ( 1 / 2 ** n)


def cube_root(y):
    s1 = sqrt_n_times(y , 2)
    s2 = s1 * sqrt_n_times(s1 , 2)
    s3 = s2 * sqrt_n_times(s2 , 4)
    s4 = s3 * sqrt_n_times(s3 , 8)
    s5 = s4 * sqrt_n_times(s4 , 16)
    s6 = s5 * sqrt_n_times(s5 , 32)
    s7 = s6 * sqrt_n_times(s6 , 64)
    return s7
    # THe resason we have to time s1 , s2 , ... is beacuse the formula is [1] + 1/ 2** n

def main():
    q = float(input())
    print(cube_root(q))

exec(input())
