N, M = map(int, input().split())
card = list(map(int, input().split()))
card.sort()
result = 0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            s = card[i] + card[j] + card[k]
            if s > M:
                break
            else:
                result = max(result, s)

print(result)