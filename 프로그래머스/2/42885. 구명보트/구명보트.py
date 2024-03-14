def solution(people, limit):
    #최대 2명과 무게제한
    ans = 0
    left, right = 0, len(people) - 1
    #전처리 필요 
    people.sort()
    
    #작은 것과 큰 것을 더해서 충분하면 그렇게 하고
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        ans += 1
    
    return ans