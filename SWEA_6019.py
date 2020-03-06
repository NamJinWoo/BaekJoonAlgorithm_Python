T = int(input())

for test_case in range(1, T+1):
    D, A, B, F = map(float, input().split())

    time = D / (A+B)
    print("#%d %.6f" %(test_case, time * F))