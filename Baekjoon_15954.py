import math
import numpy as np
N, K = input().split()
array = [int(i) for i in input().split()]
N = int(N)
K = int(K)
result = []
for k in range(K, N+1):
    for i in range(0, N - k + 1):
        average = sum(array[i:i+k]) / k
        # 분산 = 제곱의 평균 - 평균 * 평균
        a = np.array(array[i:i+k])
        a = a**2
        test = sum(a) / k

        new_average = test - average ** 2

        result.append(math.sqrt(new_average))

print("{0:.11f}".format(min(result)))
