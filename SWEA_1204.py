T = int(input())

for _ in range(T):
    test_case = int(input())
    num_list = list(map(int, input().split()))
    d = dict()
    for num in num_list:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    print("#%d %d" % (test_case, max(d, key=d.get)))
    