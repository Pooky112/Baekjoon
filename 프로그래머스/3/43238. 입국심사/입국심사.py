def solution(n, times):
    left, right = 1 , max(times) * n
    while left < right:
        mid = (left + right) // 2
        people = sum(mid // time for time in times)
        
        if people >= n:
            right = mid
            
        elif people < n:
            left = mid + 1
    
    return left