def solution(my_strings, parts):
    answer = ''
    for i, se in enumerate(parts):
        answer += my_strings[i][se[0]:se[1]+1]       
    return answer