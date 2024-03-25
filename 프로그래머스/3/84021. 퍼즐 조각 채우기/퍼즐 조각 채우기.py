def rotate(piece):
    return [(y, -x) for x, y in piece]

def translate(piece):
    min_x = min(x for x, y in piece)
    min_y = min(y for x, y in piece)
    return [(x - min_x, y - min_y) for x, y in piece]

#num은 game_board에는 0 table에는 1
def find_pieces(board, num):
    n = len(board)
    visited = set()
    find_piece = []
    
    def dfs(x, y):
        if (x, y) in visited or board[x][y] != num:
            return []
        visited.add((x, y))
        piece = [(x, y)]
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                piece.extend(dfs(nx, ny))
        return piece
    
    for x in range(n):
        for y in range(n):
            if board[x][y] == num and (x, y) not in visited:
                piece = translate(dfs(x, y))
                if piece:
                    find_piece.append(piece)
    return find_piece
        
    
    
def solution(game_board, table):
    #각각의 빈 공간과 퍼즐 조각을 찾은 후에
    #퍼즐 조각마다 돌려보면서 빈 공간과 맞는 거를 찾아보며 answer에 더해준다.
    #찾는 함수, 돌리는 함수, 기준을 맞추는 함수가 필요하다. 각각 find_pieces, rotate, translate
    answer = 0
    board_space = find_pieces(game_board, 0)
    table_pieces = find_pieces(table, 1)
    
    for piece in table_pieces:
        matched = False
        for _ in range(4):
            if matched:
                break
            piece = rotate(piece)
            piece = translate(piece)
            for i, space in enumerate(board_space):
                if sorted(space) == sorted(piece):
                    answer += len(piece)
                    board_space.pop(i)
                    matched = True
                    break
                    
    return answer 