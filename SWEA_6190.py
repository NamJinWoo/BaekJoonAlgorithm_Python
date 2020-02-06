T = int(input())

def check(num):
    for i in range(len(num)-1):
        if int(num[i]) > int(num[i+1]):
            return False

    return True

for test_case in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    answer = list()
    for i in range(N):
        for j in range(i+1,N):
            num = num_list[i] * num_list[j]
            if check(str(num)):
                answer.append(num)

    if len(answer) == 0:
        print("#%d %d" % (test_case, -1))
    else:
        print("#%d %d" % (test_case, max(answer)))