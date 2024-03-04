def solution(arr):
    while bin(len(arr))[2:].count("1") != 1:
        arr.append(0)
    return arr

"""
 a = 1
    b = len(arr)
    while a < b :
        a *= 2
    return arr + [0] * (a-b)
    """