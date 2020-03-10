T = int(input())

for test_case in range(1, T+1):
    l_list = list(map(int, input().split()))

    l_list.sort()
    answer = 0
    if l_list[0] == l_list[1]:
        answer = l_list[2]
    else:
        answer = l_list[0]

    print("#%d %d" % (test_case, answer))
    