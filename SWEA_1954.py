T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    matrix = list()
    for a in range(N):
        tmp = list()
        for b in range(N):
            tmp.append(0)
        matrix.append(tmp)
    # 처음 시작 방향
    direction = "right"
    # 현재 좌표
    current_x = 0
    current_y = 0
    for i in range(1, N*N+1):
        matrix[current_x][current_y] = i
        if direction == "right":
            if current_y == N-1 or matrix[current_x][current_y+1] != 0:
                direction = "down"
                current_x += 1
            else:
                current_y += 1
        elif direction == "down":
            if current_x == N - 1 or matrix[current_x+1][current_y] != 0:
                direction = "left"
                current_y -= 1
            else:
                current_x += 1
        elif direction == "left":
            if current_y == 0 or matrix[current_x][current_y-1] != 0:
                direction = "up"
                current_x -= 1
            else:
                current_y -= 1
        elif direction == "up":
            if current_x == 0 or matrix[current_x-1][current_y] != 0:
                direction = "right"
                current_y += 1
            else:
                current_x -= 1

    print("#"+str(test_case))
    for i in range(N):
        for j in range(N-1):
            print(matrix[i][j], end=" ")
        print(matrix[i][N-1])