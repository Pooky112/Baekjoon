import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        least = heapq.heappop(scoville)
        
        if least >= K:
            return answer
        elif not scoville:
            return -1
        
        second = heapq.heappop(scoville)
        mixed = least + second*2
        heapq.heappush(scoville, mixed)
        answer +=1
    
    return answer