def solution(arr):
    if 2 not in arr:
        return [-1]
    
    num = [i for i, x in enumerate(arr) if x == 2]
    
    return arr[min(num):max(num)+1]
    
    