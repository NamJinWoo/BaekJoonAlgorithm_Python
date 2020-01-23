import sys

def power(a,b,m):
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m

    return result

mod_num = 10 ** 9 + 7
for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    if N == 1:
        print(1)
    else:
        print(power(2,N-2,mod_num))
