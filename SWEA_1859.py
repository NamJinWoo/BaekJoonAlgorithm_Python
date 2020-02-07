T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    max_num = 0
    num_list = list(map(int, input().split()))
    total_sum = 0
    answer = 0
    for i in range(N-1, -1, -1):
        if max_num < num_list[i]:
            max_num = num_list[i]
        else:
            total_sum += max_num - num_list[i]

    print("#%d %d" % (test_case, total_sum))