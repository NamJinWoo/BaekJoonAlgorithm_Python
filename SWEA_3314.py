T = int(input())

for test_case in range(1, T+1):
    score_list = list(map(int, input().split()))

    total_sum = 0
    for score in score_list:
        if score < 40:
            total_sum += 40
        else:
            total_sum += score

    print("#%d %d" % (test_case, total_sum / len(score_list)))