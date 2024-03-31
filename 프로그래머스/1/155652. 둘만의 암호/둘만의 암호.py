def solution(s, skip, index):
    answer = ""
    alphabets = [chr(i) for i in range(ord("a"), ord("z")+1)]
    
    for char in s:
        cur_idx = alphabets.index(char)
        to_go = index
        while to_go > 0:
            cur_idx = (cur_idx+1) % 26
            if alphabets[cur_idx] not in skip:
                to_go -= 1
                
        answer += alphabets[cur_idx]
    
    return answer