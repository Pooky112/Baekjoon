def solution(n):
    answer = [[0] * n for _ in range(n)]
    r, c = 0, 0
    dr, dc = 0, 1
    
    for i in range(1, n*n + 1):
        answer[r][c] = i
        nr, nc = r + dr, c + dc
        if nr < 0 or nc < 0 or nr >= n or nc >= n or answer[nr][nc] != 0:
            dr, dc = dc, -dr  # 0 1 - 1 0 - 0 -1 - -1 0
            nr, nc = r + dr, c + dc
            
        r, c = nr, nc
        
    return answer