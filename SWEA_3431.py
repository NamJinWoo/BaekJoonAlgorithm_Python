T = int(input())

for test_case in range(1, T+1):
    L, U, X = map(int, input().split())
    answer = 0
    if L < X < U:
        answer = 0
    elif L > X:
        answer = L - X
    else:
        answer = -1

    print("#%d %d" % (test_case, answer))