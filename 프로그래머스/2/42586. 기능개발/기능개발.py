def solution(progresses, speeds):
    answer = []
    
    while progresses:
        temp = 0
        
        while progresses[0] < 100:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]

        while progresses and progresses[0] >= 100:
            temp += 1
            progresses.pop(0)
            speeds.pop(0)
        
        answer.append(temp)

        
    return answer