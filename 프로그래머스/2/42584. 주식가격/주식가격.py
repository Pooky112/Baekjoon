def solution(prices):
    """
    answer = [0] * len(prices)
    
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]:
                break

    return answer
    """
#스택
    answer = [0] * len(prices)
    stack = []
    
    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)
    
    while stack:
        top = stack.pop()
        answer[top] = len(prices) - 1 - top
    
    return answer