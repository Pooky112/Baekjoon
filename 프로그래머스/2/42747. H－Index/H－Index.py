def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort(reverse = True)
    for i, citation in enumerate(citations):
        print(i, citation)
        if i >= citation:
            return i
    return n