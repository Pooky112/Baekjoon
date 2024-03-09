import itertools

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    num_list = []
    
    for i in range(1, len(numbers) + 1):
        for per in itertools.permutations(numbers, i):
            num = int(''.join(per))
            if is_prime(num):
                num_list.append(num)
    
    
    return len(set(num_list))