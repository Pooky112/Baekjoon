def solution(arr, intervals):
    answer = []
    for a, b in intervals:
        answer.append(arr[a:b+1])
    return answer[0] + answer [1]
    