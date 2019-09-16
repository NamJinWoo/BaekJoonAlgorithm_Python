import math

N, K = map(int, input().split())
array = [int(i) for i in input().split()]
result = []

for k in range(K, N+1):
    sliced_array = array
    sum_array = []
    #누적 합 배열
    sum_array.append(array[0])
    for i in range(1, len(array)):
        sum_array.append(sum_array[i - 1] + array[i])

    sq_sum_array = []
    #누적 합 배열
    sq_sum_array.append(array[0]**2)
    for i in range(1,len(array)):
        sq_sum_array.append(sq_sum_array[i-1]+array[i]**2)

for k in range(K, N+1):
    for i in range(0, N - k + 1):
        # 분산 = 제곱의 평균 - 평균 * 평균
        var = sq_sum_array[i+k-1] / k - sum_array[i+k-1] / k

        if var >= 0:
            result.append(math.sqrt(var))


print("{0:.11f}".format(min(result)))
