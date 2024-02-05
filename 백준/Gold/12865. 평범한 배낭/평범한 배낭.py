N, K = map(int, input().split())

items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

def max_value(N, K, items):
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for w in range(1, K+1):
            # 넣을 수 있는 경우
            if items[i-1][0] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-items[i-1][0]]+ items[i-1][1])
            # 넣을 수 없는 경우
            else:
                dp[i][w] = dp[i-1][w]

    return dp[N][K]

best_value = max_value(N, K, items)
print(best_value)