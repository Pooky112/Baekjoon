def solution(m, n, puddles):
    graph = [[0] * m for _ in range(n) ]
    graph[0][0] = 1
    puddles = {(x - 1, y - 1) for x, y in puddles}
    
    for i in range(n):
        if (0, i) in puddles: break
        graph[i][0] = 1
    for j in range(m):
        if (j, 0) in puddles: break
        graph[0][j] = 1
        
    for i in range(1, n):
        for j in range(1, m):
            if (j,i) in puddles:
                continue
            
            graph[i][j] = graph[i][j-1] + graph[i-1][j]
                
    return graph[n-1][m-1] % 1000000007