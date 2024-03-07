def solution(priorities, location):
    order = 0
    queue = [(priority, i) for i, priority in enumerate(priorities)]
    
    while queue:
        cur = queue.pop(0)
        if any(cur[0] < rest[0] for rest in queue):
            queue.append(cur)
        else:
            order += 1
            if cur[1] == location:
                return order

            
        
    