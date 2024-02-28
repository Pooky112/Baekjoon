def solution(arr, queries):
    for q1, q2 in queries:
        arr[q1], arr[q2] = arr[q2], arr[q1]
    return arr