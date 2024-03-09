def solution(answers):
    num_1 = [1, 2, 3, 4, 5]
    num_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0]
    
    for i, ans in enumerate(answers):
        if ans == num_1[i % 5]:
            scores[0] += 1
    for i, ans in enumerate(answers):
        if ans == num_2[i % 8]:
            scores[1] += 1
    for i, ans in enumerate(answers):
        if ans == num_3[i % 10]:
            scores[2] += 1
    
    answer = [i + 1 for i, score in enumerate(scores) if score == max(scores)]
    
    return answer
    
