for test_case in range(1, 11):
    N = int(input())
    num_list = list(map(int, input().split()))
    answer = 0
    for i in range(2, N-2):
        height = num_list[i]
        if num_list[i-2] < height and num_list[i-1] < height and num_list[i+1] < height and num_list[i+2] < height:
            answer += height - max([num_list[i-2], num_list[i-1], num_list[i+1], num_list[i+2]])

    print("#%d %d" % (test_case, answer))
