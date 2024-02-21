from sys import stdin
from collections import deque

input = stdin.readline

def get_graph_L_water(R, C):
    graph = []
    L = []
    water = deque()
    for r in range(R):
        current_row = list(input().rstrip())
        for c, value in enumerate(current_row):
            if value == '.' or value == 'L':
                water.append((r, c))
            if value == 'L':
                L.append((r, c))
        graph.append(current_row)
    return graph, L, water

def find_swan(graph, visited, queue, L, R, C):
    next_queue = deque()
    while queue:
        i, j = queue.popleft()
        if (i, j) == L[1]:
            return True, deque()
        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj]:
                visited[ni][nj] = True
                if graph[ni][nj] == 'X':
                    next_queue.append((ni, nj))
                else:
                    queue.append((ni, nj))
    return False, next_queue
                
def melt_ice(water, graph, R, C):
    next_water = deque()
    while water:
        i, j = water.popleft()
        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < R and 0 <= nj < C and graph[ni][nj] == 'X':
                graph[ni][nj] = '.'
                next_water.append((ni, nj))
    return next_water

R, C = map(int, input().split())
graph, L, water = get_graph_L_water(R, C)
days = 0
queue = deque([L[0]])
visited = [[False] * C for _ in range(R)]
visited[L[0][0]][L[0][1]] = True

while True:
    found, next_queue = find_swan(graph, visited, queue, L, R, C)
    if found:
        break
    queue = next_queue
    water = melt_ice(water, graph, R, C)
    days += 1

print(days)
