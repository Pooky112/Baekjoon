def solution(clothes):
    cloth_table = {}
    for name, cloth in clothes:
        if cloth in cloth_table:
            cloth_table[cloth] += 1
        else:
            cloth_table[cloth] = 1
    
    answer = 1
    for count in cloth_table.values():
        print(count)
        answer *= (count + 1)
        
    return answer - 1