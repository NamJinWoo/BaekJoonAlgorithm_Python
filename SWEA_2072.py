T = int(input())

for test_case in range(1, T+1):
    num_list = list(map(int, input().split()))
    answer = 0
    for num in num_list:
        if num % 2 == 1:
            answer += num

    print("#%d %d" % (test_case, answer))

