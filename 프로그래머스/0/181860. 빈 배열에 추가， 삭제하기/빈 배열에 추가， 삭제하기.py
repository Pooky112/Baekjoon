def solution(arr, flag):
    answer = []
    for a, f in zip(arr, flag):
        if f:
            answer += [a] * a * 2
        else:
            del answer[-a:]
            
    return answer