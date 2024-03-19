def solution(N, number):
    DP = [set() for _ in range(9)]
    
    for i in range(1, 9):
        DP[i].add(int(str(N)*i))
    
    for i in range(1,9):
        for j in range(1, i):
            for a in DP[j]:
                for b in DP[i - j]:
                    DP[i].add(a - b)
                    DP[i].add(a + b)
                    DP[i].add(a * b)
                    if b != 0:
                        DP[i].add(a // b)
                        
        if number in DP[i]:
            return i
    
    return -1