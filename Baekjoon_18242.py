N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]

x, y = 0, 0
length = 0
hash_found = False

for i in range(N):
    for j in range(M):
        if not hash_found:
            if matrix[i][j] == '#':
                hash_found = True
                x, y = i, j
        else:
            if matrix[i][j] == '.':
                if j != M-1 and matrix[i][j+1] == '#':
                    continue
                length = j - y
                break
            if j == M-1:
                length = j - y + 1
                break
    else:
        continue
    break


length_half = length // 2
if matrix[x][y + length_half] == '.':
    print("UP")
elif matrix[x + length - 1][y + length_half] == '.':
    print("DOWN")
elif matrix[x + length_half][y] == '.':
    print("LEFT")
elif matrix[x + length_half][y + length - 1] == '.':
    print("RIGHT")