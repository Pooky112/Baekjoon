def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    left, right = 1, distance
    while left <= right:
        mid = (left + right) // 2
        removed = 0
        prev_rock = 0
        
        for rock in rocks:
            if rock - prev_rock < mid:
                removed +=1
            else:
                prev_rock = rock
        if removed > n:
            right = mid - 1
        else:
            left = mid + 1
    
    return right

    