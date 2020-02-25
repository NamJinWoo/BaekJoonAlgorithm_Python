T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    matrix = list()
    # 1이 있으면 저장.
    for _ in range(N):
        line = input()
        if len(matrix) != 0:
            continue
        if '1' in line:
            matrix = list(line)

    # 마지막 1 찾기
    index_1 = 0
    for i in range(len(matrix)):
        if matrix[i] == '1':
            index_1 = i

    # 최종 배열 만들기.
    final_matrix = matrix[index_1-55:index_1+1]

    # 7개씩 자르기.
    final_binary_list = list()
    binary = ""
    for i in range(len(final_matrix)):
        binary += final_matrix[i]
        if (i + 1) % 7 == 0:
            final_binary_list.append(binary)
            binary = ""

    # 0~9 까지 비교하기.
    final_num_list = list()
    for item in final_binary_list:
        if item == "0001101":
            final_num_list.append(0)
        elif item == "0011001":
            final_num_list.append(1)
        elif item == "0010011":
            final_num_list.append(2)
        elif item == "0111101":
            final_num_list.append(3)
        elif item == "0100011":
            final_num_list.append(4)
        elif item == "0110001":
            final_num_list.append(5)
        elif item == "0101111":
            final_num_list.append(6)
        elif item == "0111011":
            final_num_list.append(7)
        elif item == "0110111":
            final_num_list.append(8)
        elif item == "0001011":
            final_num_list.append(9)

    # 검증된 코드인지 확인.
    odd_sum = 0
    even_sum = 0
    for i in range(len(final_num_list)):
        if (i+1) % 2 == 1:
            odd_sum += final_num_list[i]
        else:
            even_sum += final_num_list[i]

    if (odd_sum * 3 + even_sum) % 10 == 0:
        print("#%d %d" % (test_case, sum(final_num_list)))
    else:
        print("#%d %d" % (test_case, 0))
