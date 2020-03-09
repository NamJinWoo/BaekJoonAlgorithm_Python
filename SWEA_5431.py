T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    total_set = set([i for i in range(1, N+1)])
    sub_set = set(list(map(int, input().split())))

    diff_set = total_set - sub_set
    result_list = list(diff_set)
    result_list.sort()

    print("#%d" % (test_case), end=" ")
    for i in range(len(result_list)-1):
        print(result_list[i], end=' ')
    print(result_list[-1])
