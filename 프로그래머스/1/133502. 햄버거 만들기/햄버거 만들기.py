def solution(ingredient):
    stack = []
    burger_pattern = [1, 2, 3, 1]
    burger_count = 0
    
    for ing in ingredient:
        stack.append(ing)
        if len(stack) >= 4 and stack[-4:] == burger_pattern:
            for _ in range(4):
                stack.pop()
            burger_count += 1
    return burger_count
