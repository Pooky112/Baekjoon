def build_graph(wires):
    graph = {}
    for v1, v2 in wires:
        if v1 not in graph:
            graph[v1] = []
        if v2 not in graph:
            graph[v2] = []
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph
        
def count_towers(v, graph, visited):
    visited[v] = True
    count = 1
    for i in graph[v]:
        if not visited[i]:
            count += count_towers(i, graph, visited)
    return count
    
def solution(n, wires):
    min_diff = n
    for v1, v2 in wires:
        graph = build_graph(wires)
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        
        visited = [False] * (n + 1)
        count = count_towers(v1, graph, visited)
        
        diff = abs(count- (n - count))
        min_diff = min(min_diff, diff)
        
        
    return min_diff
