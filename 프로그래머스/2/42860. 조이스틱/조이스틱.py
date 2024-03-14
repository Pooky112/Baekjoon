def solution(name):
    answer = 0
    
    #상하
    updown = [min(ord(c) - ord("A"), ord("Z") - ord(c) + 1) for c in name]
    answer += sum(updown)
    #좌우
    length = len(name)
    leftright = length - 1
    if "A" in name:
        for i in range(length):
            nex = i + 1
            while nex < length and name[nex] == "A":
                nex += 1
            distance_to_next = min(i, length - nex)
            leftright = min(leftright, i + distance_to_next + length - nex)

    answer += leftright
    return answer