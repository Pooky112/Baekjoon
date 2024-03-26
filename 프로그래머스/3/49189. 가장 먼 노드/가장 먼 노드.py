from collections import deque

def solution(n, edge):
    #1번 노드에서 가장 멀리 떨어진 노드의 갯수
    #bfs
    routes = {}
    for start, end in edge:
        routes.setdefault(start, []).append(end)
        routes.setdefault(end, []).append(start)
    
    distance = [0] * (n+1)
    visited = [False] * (n+1)
    queue = deque([1])
    visited[1] = True
    
    while queue:
        curr = queue.popleft()
        
        for next_node in routes.get(curr, []):
            if not visited[next_node]:
                visited[next_node] = True
                distance[next_node] = distance[curr] + 1
                queue.append(next_node)
                
    max_distance = max(distance)
    
    return distance.count(max_distance)