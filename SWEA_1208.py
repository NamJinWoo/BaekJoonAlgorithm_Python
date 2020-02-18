for test_case in range(1, 11):
    dump = int(input())
    num_list = list(map(int, input().split()))
    for i in range(dump):
        max_num = max(num_list)
        min_num = min(num_list)

        num_list[num_list.index(max_num)] -= 1
        num_list[num_list.index(min_num)] += 1
    answer = max(num_list) - min(num_list)
    print("#%d %d" % (test_case, answer))