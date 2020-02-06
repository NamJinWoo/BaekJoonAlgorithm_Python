T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    d = dict()
    for _ in range(N):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    P = int(input())
    # answer = list()
    print("#" + str(test_case), end=" ")
    for _ in range(P-1):
        c = int(input())
        if c in d:
            print(d[c], end=" ")
        else:
            print(0, end=" ")
    c = int(input( ))
    if c in d:
        print(d[c])
    else:
        print(0)
        # answer.append(d[c])
