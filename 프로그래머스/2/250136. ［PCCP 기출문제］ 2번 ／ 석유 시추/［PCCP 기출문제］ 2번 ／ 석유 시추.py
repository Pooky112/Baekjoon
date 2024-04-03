from collections import deque

def solution(land):
    m, n = len(land[0]), len(land)
    visited = [[False] * m for _ in range(n)]
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    col_amount = [0] * m
    
    def bfs(x, y):
        queue = deque([(x, y)])
        visited[x][y] = True
        oil_count = 1
        columns = {y}
        
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    oil_count += 1
                    columns.add(ny)
        
        for col in columns:
            col_amount[col] += oil_count
    
    
    for y in range(m):
        for x in range(n):
            if land[x][y] == 1 and not visited[x][y]:
                bfs(x, y)
    
    return max(col_amount)
