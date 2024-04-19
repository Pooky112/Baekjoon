import heapq

def solution(n, m, graph, start, end):
    distance = [float('inf')] * (n + 1)
    routes = [[] for i in range(n + 1)]

    def dijkstra(start):
        queue = []
        heapq.heappush(queue, (0, start))
        distance[start] = 0
        routes[start] = [start]

        while queue:
            cur_dist, cur_node = heapq.heappop(queue)
            if distance[cur_node] < cur_dist:
                continue

            for i in graph[cur_node]:
                cost = cur_dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    routes[i[0]] = routes[cur_node] + [i[0]]
                    heapq.heappush(queue, (cost, i[0]))



    dijkstra(start)
    print(distance[end])
    print(len(routes[end]))
    print(*routes[end])

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

solution(n, m, graph, start, end)
