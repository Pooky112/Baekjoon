def solution(triangle):
    DP = [[0] *  i for i in range(1, len(triangle)+1)]
    DP[0][0] = triangle[0][0]
    
    if len(triangle) == 1:
        return triangle[0][0]
    
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            #[i][j]의 [i+1][j+1]과 [i][j+1]의 [i+1][j] 중에서 max 더 큰 값을
            DP[i+1][j] = max(DP[i][j] + triangle[i+1][j], DP[i+1][j])
            DP[i+1][j+1] = DP[i][j] + triangle[i+1][j+1]
            
    return max(DP[len(triangle)-1])