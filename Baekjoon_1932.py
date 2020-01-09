lineCount = int(input())

t = []
for _ in range(lineCount):
    t.append(list(map(int, input().split())))

for i in range(1, lineCount):
    for j in range(len(t[i])):
        if j == 0:
            # 첫 숫자일 때.
            t[i][j] = t[i][j] + t[i-1][j]
        elif j == len(t[i])-1:
            # 마지막 숫자일 때.
            t[i][j] = t[i][j] + t[i - 1][j-1]
        else:
            # 그 외 중간에 있는 숫자일 때.
            t[i][j] = t[i][j] + max(t[i - 1][j - 1], t[i-1][j])


print(max(t[-1]))