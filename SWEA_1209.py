for test_case in range(1, 11):
    case_num = int(input())
    final_matrix = list()
    final_sum_list = list()

    # 가로 합 구하기
    for _ in range(100):
        line = list(map(int, input().split()))
        final_sum_list.append(sum(line))
        final_matrix.append(line)

    # 세로 합 구하기
    for i in range(100):
        sum_num = 0
        for j in range(100):
            sum_num += final_matrix[j][i]
        final_sum_list.append(sum_num)

    # 오른쪽 대각선 합 구하기
    sum_num = 0
    for i in range(100):
        sum_num += final_matrix[i][i]
    final_sum_list.append(sum_num)

    # 왼쪽 대각선 합 구하기:
    sum_num = 0
    for i in range(100):
        sum_num += final_matrix[i][99-i]
    final_sum_list.append(sum_num)

    print("#%d %d" % (case_num, max(final_sum_list)))