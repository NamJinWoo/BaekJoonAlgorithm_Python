N, K = map(int, input().split())

money_list = list()
for _ in range(N):
    money_list.append(int(input()))

result = 0

for i in range(1, N + 1):
    money = money_list[-i]

    if K >= money:
        num = K // money
        K -= money * num
        result += num

print(result)