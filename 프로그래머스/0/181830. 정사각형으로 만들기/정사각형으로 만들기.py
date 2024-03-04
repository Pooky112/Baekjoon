def solution(arr):
    row = len(arr)
    col = len(arr[0])
    
    if row < col:
        arr += [[0] * col for _ in range(col - row)]
    elif row > col:
        for r in arr:
            r += [0] * (row - col)
    
    return arr
