import sys
import statistics
N, K = map(int, sys.stdin.readline().split())
fullList = []
for _ in range(N):
    fullList.append(int(sys.stdin.readline()))
# fullList.sort()


# if K % 2 == 0:
#     c = K // 2
#     del fullList[:c-1]
#     del fullList[-c:]
# else:
#     c = K // 2
#     del fullList[:c]
#     del fullList[-c:]
# print(sum(fullList))
sum = 0
if K % 2 == 0:
    for i in range(N-K+1):
        slicedList = fullList[i:i+K]
        sum += statistics.median_low(slicedList)
else:
    for i in range(N - K + 1):
        slicedList = fullList[i:i + K]
        sum += statistics.median(slicedList)


print(sum)
