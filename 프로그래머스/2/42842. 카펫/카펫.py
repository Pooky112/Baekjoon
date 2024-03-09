def solution(brown, yellow):
    answer = []
    count = brown + yellow 
    for i in range(int(count**0.5), 1, -1):
        if int(i * (count / i)) == count and (i*2 + int(count/i)*2) - 4 == brown:
            w = max(i, int(count/i))
            h = min(i, int(count/i))
            
            return [w, h]
