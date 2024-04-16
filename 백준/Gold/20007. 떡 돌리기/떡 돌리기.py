import heapq

def dijkstra(start):
    distances = [float('inf') for _ in range(n)]
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, node = heapq.heappop(queue)
        if distances[node] < dist:
            continue
        for next_node, next_dist in graph[node]:
            if distances[next_node] > dist + next_dist:
                distances[next_node] = dist + next_dist
                heapq.heappush(queue, [dist + next_dist, next_node])

    return distances

def solution(distances, n):
    sorted_distances = [[distance, idx] for idx, distance in enumerate(distances)]
    sorted_distances.sort()

    if sorted_distances[-1][0] * 2 > x:
        return -1
    else:
        day = 1
        cur = 0
        for dist, i in sorted_distances:
            if cur + 2 * dist <= x:
                cur += 2 * dist
            else:
                day += 1
                cur = 2 * dist

    return day



n, m, x, y = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

distances = dijkstra(y)
print(solution(distances, n))