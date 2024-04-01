def solution(s):
    answer = []
    dic = {}
    
    for i, c in enumerate(s):
        if c in dic:
            answer.append(i - dic[c][-1])
            dic[c].append(i)
        else:
            answer.append(-1)
            dic[c] = [i]
    return answer