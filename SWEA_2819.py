T = int(input())
final_list = list()
final_set = set()

def move(i, j, alpha, count, final_list):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # 6번 이동했으면 set에 넣고 마무리.
    if count == 6:
        final_set.add(alpha)
        return

    # 4방향으로 이동.
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]

        if x < 0 or x > 3 or y < 0 or y > 3:
            continue
        # 재귀.
        move(x, y, alpha+final_list[x][y], count+1, final_list)


for test_case in range(1, T+1):
    for _ in range(4):
        final_list.append(list(input().split()))

    for i in range(4):
        for j in range(4):
            start_alpha = final_list[i][j]
            # 재귀 시작
            move(i, j, start_alpha, 0, final_list)
    print("#%d %d" % (test_case, len(final_set)))
    # 초기화.
    final_list = list()
    final_set = set()