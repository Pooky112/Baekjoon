def solution(str1, str2):
    arr = [a + b for a, b in zip(str1, str2)]
    return ''.join(arr)