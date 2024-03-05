def solution(picture, k):
    answer = []
    for p in picture:
        expanded = ''.join(c * k for c in p)
        print(expanded)
        for _ in range(k):
            answer.append(expanded)
    
    return answer