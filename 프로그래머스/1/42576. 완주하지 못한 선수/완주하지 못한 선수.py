from collections import Counter

def solution(participant, completion):
    par = Counter(participant)
    com = Counter(completion)
    
    return list((par - com).keys())[0]