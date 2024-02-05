import sys

N, K = map(int, sys.stdin.readline().split())
items = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]

def max_value(N, K, items):
    """
    N = number of items
    K = Maximum weight capacity
    items = (weight, value) of item
    """
    dp = [0]*(K + 1)

    for item_index in range(N):
        for current_weight in range(K, items[item_index][0]- 1, -1):
            dp[current_weight] = max(dp[current_weight], dp[current_weight - items[item_index][0]] + items[item_index][1])

    return dp[K]

best_value = max_value(N, K, items)
print(best_value)