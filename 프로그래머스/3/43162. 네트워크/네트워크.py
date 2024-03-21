def dfs(node, visited, computers):
    visited[node] = True
    for i, connected in enumerate(computers[node]):
        if connected == 1 and not visited[i]:
            dfs(i, visited, computers)

def solution(n, computers):
    visited = [False] * n
    network = 0

    for i in range(n):
        if not visited[i]:
            dfs(i, visited, computers)
            network += 1  
    return network
