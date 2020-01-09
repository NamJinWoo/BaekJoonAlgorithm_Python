wines = int(input())
wine_list = [0]
for _ in range(wines):
    wine_list.append(int(input()))

dp = [0 for _ in range(wines+1)]

# 1번으로 시작하거나 1번 2번으로 시작하거나
if wines == 1:
    dp[1] = wine_list[1]
else:
    dp[1] = wine_list[1]
    dp[2] = wine_list[1] + wine_list[2]

# 3가지 경우
# i번째, i-1번째 와인 둘다 마시는 경우
# i-1번째 마시고 i번째 와인 안미시는 경우
# i번째 마시고 i-1째 안마시는 경우
# 최댓값을 구하는 경로이기 때문에 둘다 안마시는 경우는 제외.

for i in range(3, wines+1):
    dp[i] = max(wine_list[i] + wine_list[i-1] + dp[i-3], dp[i-1], wine_list[i] + dp[i-2])

print(dp[-1])