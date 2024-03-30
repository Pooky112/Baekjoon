def solution(keymap, targets):
    answer = []
    
    for target in targets:
        total_num = 0
        for char in target:
            flag = False
            time = 101
            for key in keymap:
                if char in key:
                    time = min(key.index(char) + 1, time)
                    flag = True
            if not flag:
                total_num = -1;break
            
            total_num += time
        
        answer.append(total_num)
        
    return answer