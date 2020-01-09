n = int(input())
num_list = [0]
num_list += list(map(int, input().split()))

dp = [0 for _ in range(n+1)]
result = -1001
for i in range(1, n+1):
    dp[i] = max(dp[i-1] + num_list[i], num_list[i])
    result = max(result, dp[i])

print(result)