def solution(storey):
    answer = 0
    
    while storey:
        one = storey % 10
        
        if one > 5:
            answer += (10 - one)
            storey += 10
        elif one < 5:
            answer += one
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += one
        
        storey //= 10
    
    return answer