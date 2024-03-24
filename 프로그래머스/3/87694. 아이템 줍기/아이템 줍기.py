from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    #2배를 해주어 정확도를 높여주는 것
    grid = [[0] * 101 for _ in range(101)] # 1 x 1 격자로 좌표를 확장
    visited = [[False] * 101 for _ in range(101)] # 방문 여부를 확인할 배열
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1 * 2, x2 * 2 + 1): # 격자 확장을 위해 x 좌표를 2배로 늘림
            for j in range(y1 * 2, y2 * 2 + 1): # 격자 확장을 위해 y 좌표를 2배로 늘림
                # 직사각형의 내부 + 경계를 1로 설정
                grid[i][j] = 1
                
    # 직사각형의 경계만을 1로 설정
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1 * 2, x2 * 2 + 1):
            for j in range(y1 * 2, y2 * 2 + 1):
                # 내부를 0으로 다시 설정
                if x1 * 2 < i < x2 * 2 and y1 * 2 < j < y2 * 2:
                    grid[i][j] = 0
                    
    # BFS로 최단거리 찾기
    queue = deque([(characterX * 2, characterY * 2)])
    visited[characterX * 2][characterY * 2] = True
    distance = 0
    
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if x == itemX * 2 and y == itemY * 2:
                return distance // 2 # 격자 확장을 위해 거리를 2로 나눔
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 101 and 0 <= ny < 101 and not visited[nx][ny] and grid[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
        distance += 1

    return -1  # 경로를 찾을 수 없는 경우
