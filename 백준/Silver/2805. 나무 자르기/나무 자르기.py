
def solution(n, m, tree):
    low = 0
    high = max(tree)
    height = []

    while low <= high:
        mid = (low + high) // 2
        target = 0
        for i in range(n):
            if tree[i] - mid >= 0:
                target += tree[i] - mid
        if target < m:
            high = mid - 1
        else:
            height.append(mid)
            low = mid + 1
    return max(height)

n, m = map(int, input().split())
tree = list(map(int, input().split()))

print(solution(n, m, tree))
