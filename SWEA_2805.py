T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    final_square = list()
    answer = 0
    for _ in range(N):
        sub_list = list(map(int, input()))
        final_square.append(sub_list)

    index = int(N/2)
    reverse = False

    for i in range(N):
        if not reverse:
            s_list = final_square[i][index-i:N-(index-i)]
            answer += sum(s_list)
            if index - i == 0:
                reverse = True
        else:
            s_list = final_square[i][i-index:N-(i-index)]
            answer += sum(s_list)
    print("#%d %d" % (test_case, answer))
