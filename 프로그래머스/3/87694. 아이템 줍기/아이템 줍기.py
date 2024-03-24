from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    #2배를 해주어 정확도를 높여주어야 한다. 완전히 겹치지는 않더라도 맞닿을 경우
    #잘못된 길을 통해서 갈 수 있기 때문에 제대로 된 답이 나오지 않을 수가 있음
    #visited를 사용하지 않는 방법은?
    graph = [[0] * 101 for _ in range(101)]
    #visited = [[False] * 101 for _ in range(101)]
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1 * 2, x2 *2 + 1):
            for j in range(y1 * 2, y2 * 2 + 1):
                if x1 * 2 < i < x2 * 2 and y1 * 2 < j < y2 * 2:
                    graph[i][j] = -1
                elif graph[i][j] != -1:
                    graph[i][j] = 1
                
    queue = deque([(characterX * 2, characterY * 2)])
    graph[characterX * 2][characterY * 2] = 2
    distance = 0
    
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if x == itemX * 2 and y == itemY * 2:
                return distance // 2 # 격자 확장을 위해 거리를 2로 나눔
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 101 and 0 <= ny < 101 and graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = 2
        distance += 1

    return -1  # 경로를 찾을 수 없는 경우


"""
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    grid = [[0] * 101 for _ in range(101)]  # 0으로 초기화된 그리드
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1 * 2, x2 * 2 + 1):
            for j in range(y1 * 2, y2 * 2 + 1):
                if x1 * 2 < i < x2 * 2 and y1 * 2 < j < y2 * 2:
                    grid[i][j] = -1  # 내부를 -1로 설정
                elif grid[i][j] != -1:  # 내부가 아니면 경로(외곽)로 설정
                    grid[i][j] = 1
    
    queue = deque([(characterX * 2, characterY * 2)])
    grid[characterX * 2][characterY * 2] = 2  # 시작 위치를 방문했다고 표시
    distance = 0
    
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if x == itemX * 2 and y == itemY * 2:
                return distance // 2  # 격자 확장을 위해 거리를 2로 나눔
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 101 and 0 <= ny < 101 and grid[nx][ny] == 1:  # 방문하지 않은 경로일 경우
                    queue.append((nx, ny))
                    grid[nx][ny] = 2  # 방문했다고 표시
        distance += 1

    return -1  # 경로를 찾을 수 없는 경우
"""