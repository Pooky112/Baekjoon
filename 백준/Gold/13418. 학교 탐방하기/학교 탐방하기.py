import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

def calculate_fatigue(n, edges, reverse = False):
    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)
    edges = sorted(edges, key = lambda x: x[2], reverse = reverse)
    fatigue = 0
    for a, b, c in edges:
        if find(parent, a) != find(parent, b):
            union(parent, rank, a, b)
            if c == 0:
                fatigue += 1
    return fatigue**2

n, m = map(int, sys.stdin.readline().split())
edges = []
for i in range(m + 1):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((a, b, c))

worst_fatigue = calculate_fatigue(n, edges, reverse = False)
best_fatigue = calculate_fatigue(n, edges, reverse = True)

print(worst_fatigue - best_fatigue)
