H, M = map(int, input().split())

if 45 <= M <= 59:
    print("{} {}".format(H, M-45))
else:
    if H == 0:
        print("{} {}".format(23, M + 15))
    else:
        print("{} {}".format(H-1, M + 15))