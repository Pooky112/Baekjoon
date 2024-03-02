def solution(arr):
    answer = []
    for i, num in enumerate(arr):
        if num == 2:
            answer.append(i)
    
    if len(answer) >= 2:
        return arr[answer[0]:answer[-1]+1]
    elif len(answer) == 1:
        return [arr[answer[0]]]
    else:
        return [-1]
    
    