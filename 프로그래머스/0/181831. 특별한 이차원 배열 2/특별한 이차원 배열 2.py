def solution(arr):
    row = len(arr)
    col = len(arr[0])
    for i in range(row):
        for j in range(col):
            if arr[i][j] != arr[j][i]:
                return 0
    
    return 1