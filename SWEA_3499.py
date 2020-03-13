T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    total_list = list(input().split())
    index = int(N / 2)
    answer = list()
    if N % 2 == 0:
        sub_list1 = total_list[0: index]
        sub_list2 = total_list[index: N]

        for i in range(len(sub_list2)):
            answer.append(sub_list1[i])
            answer.append(sub_list2[i])
    else:
        sub_list1 = total_list[0: index + 1]
        sub_list2 = total_list[index + 1: N]
        for i in range(len(sub_list2)):
            answer.append(sub_list1[i])
            answer.append(sub_list2[i])
        answer.append(sub_list1[-1])

    print("#%d" % test_case, end=' ')
    for i in range(len(answer)-1):
        print(answer[i], end=' ')
    print(answer[-1])
