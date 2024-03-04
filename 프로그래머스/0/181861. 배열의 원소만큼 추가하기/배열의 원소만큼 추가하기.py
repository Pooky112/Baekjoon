def solution(arr):
    answer = []
    
    for c in arr:
        answer += [c] * c
    return answer