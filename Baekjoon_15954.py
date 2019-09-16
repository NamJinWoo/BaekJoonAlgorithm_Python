import math

def funcMap(n):
    return n * n


N, K = map(int, input().split())
array = [int(i) for i in input().split()]
result = []
for k in range(K, N+1):
    for i in range(0, N - k + 1):
        average = sum(array[i:i+k]) / k
        # 분산 = 제곱의 평균 - 평균 * 평균
        m = list(map(funcMap, array[i:i+k]))

        test = sum(m) / k

        new_average = test - average ** 2
        if new_average >= 0:
            result.append(math.sqrt(new_average))


print("{0:.11f}".format(min(result)))
