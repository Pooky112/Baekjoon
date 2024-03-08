def solution(numbers):
    answer = ''
    temp = []

    for i, num in enumerate(numbers):
        temp.append((str(num) * 3, i))
    
    for _, i in sorted(temp)[::-1]:
        answer += str(numbers[i])
        
    return answer if answer[0] != '0' else '0'

"""
str_numbers = list(map(str, numbers))
str_numbers.sort(key:lambda x: x*3, reverse = True)
answer = ''.join(str_numbers)

"""