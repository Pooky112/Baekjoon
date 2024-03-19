def solution(triangle):
    DP = [[0] *  i for i in range(1, len(triangle)+1)]
    DP[0][0] = triangle[0][0]
    
    height = len(triangle)
    
    #거꾸로 해서 올라가는 게 시간이 더 빠름, 새로운 리스트 안 만들어도 되고, 그냥 triangle 고치면 된다.
    for i in range(height-1):
        for j in range(len(triangle[i])):
            #[i][j]의 [i+1][j+1]과 [i][j+1]의 [i+1][j] 중에서 max 더 큰 값을
            DP[i+1][j] = max(DP[i][j] + triangle[i+1][j], DP[i+1][j])
            DP[i+1][j+1] = DP[i][j] + triangle[i+1][j+1]
            
    return max(DP[height-1])