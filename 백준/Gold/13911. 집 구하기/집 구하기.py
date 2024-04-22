import heapq
import sys
from collections import defaultdict

def dijkstra(start_nodes):
    distance = [float('inf')] * (V+1)
    queue = []
    for node in start_nodes:
        distance[node] = 0
        heapq.heappush(queue, (0, node))
    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for next_dist, next_node in routes[node]:
            if dist + next_dist < distance[next_node]:
                distance[next_node] = dist + next_dist
                heapq.heappush(queue, (dist + next_dist, next_node))

    return distance

V, E = map(int, sys.stdin.readline().split())
routes = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    routes[u].append((w, v))
    routes[v].append((w, u))
M, x = map(int, sys.stdin.readline().split())
M_nodes = list(map(int, sys.stdin.readline().split()))
S, y = map(int, sys.stdin.readline().split())
S_nodes = list(map(int, sys.stdin.readline().split()))

distance1 = dijkstra(M_nodes)
distance2 = dijkstra(S_nodes)

answer = float('inf')
for i in range(1, V+1):
    if i not in M_nodes and i not in S_nodes and distance1[i] <= x and distance2[i] <= y:
        answer = min(answer, distance1[i] + distance2[i])

if answer != float('inf'):
    print(answer)
else:
    print(-1)

