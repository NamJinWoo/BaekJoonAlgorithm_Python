from collections import deque
T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    one_side = int(N / 4)

    num_deque = deque(list(input()))

    total_num = list()
    for i in range(one_side):
        num_list = list(num_deque)
        for j in range(0, len(num_deque), one_side):
            num_str = ''.join(num_list[j:j+one_side])
            if int(num_str,16) not in total_num:
                total_num.append(int(num_str,16))
        num_deque.rotate(1)

    total_num.sort(reverse=True)
    print("#%d %d" % (test_case, total_num[K-1]))

