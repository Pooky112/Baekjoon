import sys
from collections import deque
from itertools import combinations

def solution(graph, N, M):
    answer = float('inf')
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    loc_2 = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                loc_2.append((i, j))
    number_of_1 = 0
    for i in range(N):
        number_of_1 += graph[i].count(1)


    combi = list(combinations(loc_2, M))

    queue = deque()

    for comb in combi:
        visited = [[-1] * N for _ in range(N)]
        for com in comb:
            queue.append(com)
        for i in range(M):

            visited[comb[i][0]][comb[i][1]] = 0
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not graph[nx][ny] == 1:
                    if visited[nx][ny] == -1 or visited[nx][ny] > visited[x][y] + 1:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))

        count = 0
        for i in range(N):
            count += visited[i].count(-1)
        if count != number_of_1:
            continue

        max_val = 0
        for i in range(N):
            for j in range(N):
                max_val = max(max_val, visited[i][j])

        answer = min(answer, max_val)

    return -1 if answer == float('inf') else answer


N, M = map(int, sys.stdin.readline().split())
graph = []
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))

print(solution(graph, N, M))

