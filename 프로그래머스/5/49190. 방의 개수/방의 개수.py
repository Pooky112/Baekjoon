from collections import defaultdict

def solution(arrows):
    path = defaultdict(int)
    moves = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    visited = set()
    
    x, y = 0, 0
    visited.add((x, y))
    
    answer = 0
    for arrow in arrows:
        for _ in range(2): 
            nx, ny = x + moves[arrow][0], y + moves[arrow][1]
            if path[(x, y, nx, ny)] == 0:
                path[(x, y, nx, ny)] = 1
                path[(nx, ny, x, y)] = 1
                if (nx, ny) in visited: 
                    answer += 1
                else:
                    visited.add((nx, ny))
            else:  
                path[(x, y, nx, ny)] += 1
                path[(nx, ny, x, y)] += 1
            x, y = nx, ny
            
    return answer
