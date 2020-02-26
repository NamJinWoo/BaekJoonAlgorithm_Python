def power(num, a, n, cnt):
    if cnt == n:
        return num

    num = num * a
    return power(num, a, n, cnt + 1)


for _ in range(10):
    test_case = int(input())
    a, n = map(int, input().split())
    result = power(1, a, n, 0)
    print("#%d %d" % (test_case, result))