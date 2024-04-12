
def solution(N, G):
    routes = {i: set() for i in range(N)}
    for i in range(N):
        for j in range(N):
            if G[i][j] == 1:
                routes[i].add(j)

    for i in routes.keys():
        stack = []
        visited = [False] * N
        stack.extend(routes[i])

        while stack:
            cur = stack.pop()
            if not visited[cur]:
                visited[cur] = True
                routes[i].add(cur)
                stack.extend(routes.get(cur, []))

    for i, val in routes.items():
        for j in val:
            G[i][j] = 1

    return G

N = int(input())
G = []
for i in range(N):
    G.append(list(map(int, input().split())))

G = solution(N, G)
for i in range(N):
    for j in range(N):
        print(G[i][j], end=" ")
    print()



