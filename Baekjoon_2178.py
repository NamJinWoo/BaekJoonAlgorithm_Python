from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
map_list = [list(map(int, list(input()))) for _ in range(N)]
queue = deque()
checklist = [[False] * M for _ in range(N)]
route = [[0] * M for _ in range(N)]

queue.append((0, 0))
checklist[0][0] = True
route[0][0] = 1

while queue:
    x, y = queue.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if checklist[nx][ny] is False and map_list[nx][ny] == 1:
                queue.append((nx, ny))
                route[nx][ny] = route[x][y] + 1
                checklist[nx][ny] = True

print(route[N - 1][M - 1])