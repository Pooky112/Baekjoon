def solution(str_list):
    l = str_list.index("l") if "l" in str_list else len(str_list)
    r = str_list.index("r") if "r" in str_list else len(str_list)
    if l < r:
        return str_list[:l]   
    elif r < l:
        return str_list[r+1:]
    else:
        return []
    
    
        
    