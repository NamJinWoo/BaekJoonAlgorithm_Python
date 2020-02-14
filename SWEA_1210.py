for _ in range(10):
    test_case = int(input())
    ladder = list()
    for i in range(100):
        ladder.append(list(map(int, input().split())))
    # 2가 있는 지점.
    destination = ladder[-1].index(2)
    # 시작 지점.
    current_x = 98
    current_y = destination

    answer = 0

    rotate_x = [0, 0]
    rotate_y = [1, -1]
    while True:
        turn = False
        # 좌우를 먼저 확인.
        for i in range(2):
            tmp_x = current_x + rotate_x[i]
            tmp_y = current_y + rotate_y[i]
            # 범위를 넘어가면 패스.
            if tmp_y < 0 or tmp_y > 99:
                continue

            if ladder[tmp_x][tmp_y] == 1:
                # 다시 돌아가지 않게 0으로 바꿈.
                ladder[current_x][current_y] = 0
                current_x = tmp_x
                current_y = tmp_y
                turn = True
        if not turn:
            current_x = current_x-1

        if current_x == 0:
            answer = current_y
            break
    print("#%d %d" % (test_case, answer))
