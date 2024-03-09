def solution(answers):
    answer = []
    num_1 = [1, 2, 3, 4, 5] * (len(answers)// 5 + 1)
    num_2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers)// 8 + 1)
    num_3 = [3, 3, 1, 1,2,  2,4, 4,5, 5] * (len(answers)// 5 + 1)
    a, b, c = 0, 0, 0
    for val, ans in zip(num_1[:len(answers)], answers):
        print("a", val, ans)
        if val == ans:
            a += 1
    for val, ans in zip(num_2[:len(answers)], answers):
        print("b", val, ans)
        if val == ans:
            b += 1
    for val, ans in zip(num_3[:len(answers)], answers):
        print("c", val, ans)
        if val == ans:
            c += 1
    
    if max(a,b,c) == a:
        answer.append(1)
    if max(a,b,c) == b:
        answer.append(2)
    if max(a,b,c) == c:
        answer.append(3)
    
    
    return answer
    
