def solution(my_string, is_suffix):
    suffix = my_string[-len(is_suffix):]
    
    return 1 if suffix == is_suffix else 0
"""
def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))
"""