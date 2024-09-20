import sys
from collections import deque

N = int(sys.stdin.readline())

house = [list(sys.stdin.readline().strip()) for _ in range(N)]

doors = []

for i in range(N):
    for j in range(N):
        if house[i][j] == '#':
            doors.append((i, j))

start = doors[0]
end = doors[1]

visited = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]

queue = deque()
for dir in range(4):
    visited[start[0]][start[1]][dir] = 0
    queue.append((start[0], start[1], dir))

directions = [(-1, 0), (0,1), (1,0), (0, -1)]

while queue:
    x, y, dir = queue.popleft()
    nx = x + directions[dir][0]
    ny = y + directions[dir][1]
    while 0 <= nx < N and 0 <= ny < N:
        if house[nx][ny] == "*":
            break
        if visited[nx][ny][dir] > visited[x][y][dir]:
            visited[nx][ny][dir] = visited[x][y][dir]
            queue.appendleft((nx, ny, dir))
        if house[nx][ny] == "!":
            for dir2 in [(dir + 1) % 4, (dir + 3) % 4]:
                if visited[nx][ny][dir2] > visited[x][y][dir] + 1:
                    visited[nx][ny][dir2] = visited[x][y][dir] + 1
                    queue.append((nx, ny, dir2))


        nx += directions[dir][0]
        ny += directions[dir][1]

min_mirrors = min(visited[end[0]][end[1]])
print(min_mirrors)