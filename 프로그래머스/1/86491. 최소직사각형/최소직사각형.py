def solution(sizes):
    s = []
    for size in sizes:
        width = max(size)
        height = min(size)
        s.append([width, height])
    
    return max(s)[0] * (max(h[1] for h in s))
    
        
        
