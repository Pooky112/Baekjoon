def solution(n, lost, reserve):
    after_reserve = [r for r in reserve if r not in lost]
    after_lost = [l for l in lost if l not in reserve]
    
    for r in sorted(after_reserve):
        if r - 1 in after_lost:
            after_lost.remove(r-1)
        elif r  + 1 in after_lost:
            after_lost.remove(r+1)
        
    return n - len(after_lost)
