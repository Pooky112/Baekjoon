# def solution(triangle):
#     DP = [[0] *  i for i in range(1, len(triangle)+1)]
#     DP[0][0] = triangle[0][0]
    
#     height = len(triangle)
    
#     if height == 1:
#         return triangle[0][0]
    
#     for i in range(height-1):
#         for j in range(len(triangle[i])):
#             #[i][j]의 [i+1][j+1]과 [i][j+1]의 [i+1][j] 중에서 max 더 큰 값을
#             DP[i+1][j] = max(DP[i][j] + triangle[i+1][j], DP[i+1][j])
#             DP[i+1][j+1] = DP[i][j] + triangle[i+1][j+1]
            
#     return max(DP[height-1])

def solution(triangle):
    # 삼각형의 높이
    height = len(triangle)
    
    # 바닥부터 두 번째 줄까지 내려오면서 각 단계의 최대값을 갱신
    for i in range(height - 2, -1, -1):
        for j in range(i + 1):
            # 현재 위치에서 내려갈 수 있는 두 경로 중 더 큰 합을 선택
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    
    # 꼭대기에서 바닥까지 내려왔을 때 최대값
    return triangle[0][0]
