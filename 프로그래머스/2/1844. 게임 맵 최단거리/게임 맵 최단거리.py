from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    distance = [[-1] * m for _ in range(n)]
    distance[0][0] = 1
    
    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0<= ny < m and maps[x][y] == 1 and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
    
    print(distance)
    return distance[n-1][m-1]