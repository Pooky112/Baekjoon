def solution(rank, attendance):
    filtered = sorted([(r, i) for i, r in enumerate(rank) if attendance[i]])
    a = filtered[0][1]
    b = filtered[1][1]
    c = filtered[2][1]
    
    return 10000*a + 100*b + c