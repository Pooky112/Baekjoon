import heapq

def solution(jobs):
    answer = 0
    jobs.sort()
    heap = []
    
    time, start = 0, -1
    count = 0
    while count < len(jobs):
        for job in jobs:
            if start < job[0] <= time:
                heapq.heappush(heap, (job[1], job[0]))
        if heap:
            count += 1
            current = heapq.heappop(heap)
            start = time 
            time += current[0] # 현재 시간
            answer += time - current[1] # 요청에서 종료까지
        else:
            time += 1
    return answer // count
