import math

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(a, b):
    a, b = find(a), find(b)
    min_P, max_P = min(a, b), max(a, b)
    parent[max_P] = min_P

def solution(n, m, gods, links):
    for i in range(n):
        for j in range(i+1, n):
            if find(i+1) != find(j+1):
                links.append((math.sqrt((gods[i][0]-gods[j][0])**2+(gods[i][1]-gods[j][1])**2), i+1, j+1))

    links.sort()
    answer = 0
    for w, a, b in links:
        if find(a) != find(b):
            union(a, b)
            answer += w

    print(f"{answer:.2f}")

n, m = map(int, input().split())
gods = []
links = []
parent = [i for i in range(n+1)]
for _ in range(n):
    x, y = map(int, input().split())
    gods.append((x, y))
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)


solution(n, m, gods, links)