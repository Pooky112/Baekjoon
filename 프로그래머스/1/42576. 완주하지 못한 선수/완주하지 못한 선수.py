#from collections import Counter

def solution(participant, completion):
    #par = Counter(participant)
    #com = Counter(completion)
    
    #return list((par - com).keys())[0]
    h_table = {}
    for name in participant:
        if name in h_table:
            h_table[name] += 1
        else:
            h_table[name] = 1
    
    for name in completion:
        h_table[name] -= 1
        
    for name, count in h_table.items():
        if count > 0:
            return name



"""
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer"""