import sys

n = int(sys.stdin.readline())
papers = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def count_papers(papers, x, y, n):
    global blue, white

    initial_color = papers[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if papers[i][j] != initial_color:
                next_n = n // 2
                count_papers(papers, x, y, next_n)
                count_papers(papers, x + next_n, y, next_n)
                count_papers(papers, x, y + next_n, next_n)
                count_papers(papers, x + next_n, y + next_n, next_n)
                return
            
    if initial_color == 0:
        white += 1
    else:
        blue += 1
blue = 0
white = 0
count_papers(papers, 0, 0, n)
print(white)
print(blue)

