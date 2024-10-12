def solution(num_list):
    even = int(''.join(str(x) for x in num_list if x % 2 == 0))
    odd = int(''.join(str(x) for x in num_list if x % 2 == 1))
    return even + odd