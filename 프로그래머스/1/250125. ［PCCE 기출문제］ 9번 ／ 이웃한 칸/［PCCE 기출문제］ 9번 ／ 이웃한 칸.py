def solution(board, h, w):
    answer = 0
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    for dx, dy in directions:
        nx, ny = h + dx, w + dy
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
            if board[nx][ny] == board[h][w]:
                answer += 1
    return answer