def solution(numbers, target):
    #재귀함수 정의
    def count_targets(index, curr_sum):
        if index == len(numbers):
            return 1 if curr_sum == target else 0
    
        count = 0
        count += count_targets(index + 1, curr_sum + numbers[index])
        count += count_targets(index + 1, curr_sum - numbers[index])
        return count
    
    
    return count_targets(0, 0)