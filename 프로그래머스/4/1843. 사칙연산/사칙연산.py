def solution(arr):
    #숫자와 연산자 분리
    numbers = [int(s) for s in arr[::2]]
    operators = arr[1:len(arr):2]
    
    n = len(numbers)
    dp = [[(0, 0) for _ in range(n)] for _ in range(n)]
    
    #초기화
    for i in range(n):
        dp[i][i] = (numbers[i], numbers[i])
    
    #길이
    for l in range(2, n + 1):
        #시작점
        for i in range(n - l + 1):
            #끝점
            j = i + l - 1
            min_val, max_val = float('inf'), float('-inf')
            for k in range(i,j):
                op = operators[k]
                left = dp[i][k]
                right = dp[k+1][j]
                if op == '+':
                    min_val = min(min_val, left[0] + right[0])
                    max_val = max(max_val, left[1] + right[1])
                else:
                    min_val = min(min_val, left[0] - right[1])
                    max_val = max(max_val, left[1] - right[0])
            dp[i][j] = (min_val, max_val)
    
    return dp[0][n - 1][1]
                    