def solution(l, r):    
    res = []
    for num in range(l, r + 1):
        str_num = str(num)
        if all(x in '05' for x in str_num):
            res.append(num)
    
    return res if res else [-1]

"""
 answer = []
    i = 1
    n = 5

    while True:
        if n > r: break
        n = 5 * int(bin(i)[2:])
        if l <= n <= r:
            answer.append(n)
        i += 1

    return [-1] if len(answer) == 0 else answer
"""