def solution(s):
    answer = 0
    first = 0
    others = 0
    index = 0
    
    for i, c in enumerate(s):
        if first == 0:
            first += 1
            index = i
        else:
            if c == s[index]:
                first += 1
            else:
                others += 1
                if others == first:
                    answer += 1
                    first = 0
                    others = 0
                
    if others > 0 or first > 0:
        answer += 1
        
    return answer