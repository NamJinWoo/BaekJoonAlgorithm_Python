T = int(input())

for test_case in range(1, T+1):
    N = int(input().split()[1])
    alpha_to_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    result_list = list()

    line = input().split()
    for alpha in alpha_to_num:
        for _ in range(line.count(alpha)):
            result_list.append(alpha)
    print("#%d" % test_case)
    for i in range(len(result_list)-1):
        print(result_list[i], end=" ")
    print(result_list[-1])