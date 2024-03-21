def solution(numbers, target):
    def count_targets(index, curr_sum):
        if index == len(numbers):
            return 1 if curr_sum == target else 0
        
        return count_targets(index + 1, curr_sum + numbers[index]) + count_targets(index + 1, curr_sum - numbers[index])
    
    
    return count_targets(0, 0)

"""
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
"""