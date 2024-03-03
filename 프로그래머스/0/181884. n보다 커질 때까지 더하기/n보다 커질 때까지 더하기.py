def solution(numbers, n):
    sum_num = 0
    for num in numbers:
        sum_num += num
        if sum_num > n:
            return sum_num