import heapq as hq

def solution(operations):
    answer = []
    min_heap = []
    max_heap = []
    
    for op in operations:
        I, num = op.split()
        #최소힙은 그대로 
        #최대힙은 마이너스 붙여서
        if I == "I":
            hq.heappush(min_heap, int(num))
            hq.heappush(max_heap, -int(num))
        else:
            if num == "1" and max_heap:
                temp = hq.heappop(max_heap)
                min_heap.remove(-temp)
            elif num == "-1" and min_heap:
                temp = hq.heappop(min_heap)
                max_heap.remove(-temp)

    if not max_heap or not min_heap: 
        return [0,0]
    else:
        max_num = -hq.heappop(max_heap)
        min_num = hq.heappop(min_heap)
        return [max_num, min_num]
