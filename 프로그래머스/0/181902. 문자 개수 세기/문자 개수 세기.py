def solution(my_string):
    answer = [0] * 52
    
    for c in my_string:
        if 'A' <= c <= 'Z':
            i = ord(c) - ord('A')
        elif 'a' <= c <= 'z':
            i = ord(c) - ord('a') + 26
        
        answer[i] += 1
    
    return answer