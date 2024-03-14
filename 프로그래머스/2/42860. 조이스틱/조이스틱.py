def solution(name):
    answer = 0
    
    #상하
    updown = [min(ord(c) - ord("A"), ord("Z") - ord(c) + 1) for c in name]
    answer += sum(updown)
    #좌우
    length = len(name)
    leftright = length - 1
    for i in range(length):
        next = i + 1
        while next < length and name[next] == "A":
            next += 1
        distance_to_next = min(i, length - next)
        leftright = min(leftright, i + distance_to_next + length - next)
    
    answer += leftright
    return answer