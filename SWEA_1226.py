def move(matrix, start_point, answer):
    # 4방향 구하기.
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    current_point = start_point
    for i in range(4):
        if matrix[current_point[0] + dx[i]][current_point[1] + dy[i]] == 0:
            # 현재 위치 변경 후 재귀
            matrix[current_point[0] + dx[i]][current_point[1] + dy[i]] = 1
            start_point = [current_point[0] + dx[i], current_point[1] + dy[i]]
            move(matrix, start_point, answer)

        # end_point를 찾았을 때
        elif matrix[current_point[0] + dx[i]][current_point[1] + dy[i]] == 3:
            answer.append(1)


for _ in range(10):
    test_case = int(input())
    matrix = list()
    for x in range(16):
        line = list(map(int, input()))
        matrix.append(line)

        # 시작점을 나타냄.
        if 2 in line:
            start_point = [x, line.index(2)]
    answer = []
    move(matrix, start_point, answer)

    #가는 길목에 3이 있었으면,
    if 1 in answer:
        print("#%d %d" % (test_case, 1))
    else:
        print("#%d %d" % (test_case, 0))
