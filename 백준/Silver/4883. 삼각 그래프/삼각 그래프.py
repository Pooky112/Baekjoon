import sys

def shortest_path():
    K = 1
    while True:
        N = int(sys.stdin.readline())
        if N == 0:
            break
        graph = []
        for i in range(N):
            graph.append(list(map(int, sys.stdin.readline().strip().split())))

        graph[1][0] += graph[0][1]
        graph[1][1] += min(graph[0][1], graph[0][1] + graph[0][2], graph[1][0])
        graph[1][2] += min(graph[0][1], graph[0][1] + graph[0][2], graph[1][1])

        for i in range(2, N):
            graph[i][0] += min(graph[i-1][0], graph[i-1][1])
            graph[i][1] += min(graph[i-1][0], graph[i-1][1], graph[i - 1][2], graph[i][0])
            graph[i][2] += min(graph[i-1][1], graph[i-1][2], graph[i][1])

        print(f"{K}. {graph[-1][1]}")
        K += 1

shortest_path()