import itertools

def solution(clothes):
    #answer = 0
    cloth_table = {}
    for name, cloth in clothes:
        if cloth in cloth_table:
            cloth_table[cloth] += 1
        else:
            cloth_table[cloth] = 1
    #val = list(cloth_table.values())
    
    #for i in range(1, len(cloth_table)+1):
     #   temp = list(itertools.combinations(val, i))
      #  for j in range(len(temp)):
       #     answer += temp[j][0]
    answer = 1
    for count in cloth_table.values():
        answer *= (count + 1)
        
    return answer - 1