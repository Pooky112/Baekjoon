import sys

N = int(sys.stdin.readline())
ans = 0
row = [-1] * N

def is_safe(n):
    for i in range(n):
        if row[n] == row[i] or abs(row[n] - row[i]) == abs(n - i):
            return False

    return True


def n_queen(n):
    global ans
    if n == N:
        ans += 1
        return

    else:
        for i in range(N):
            row[n] = i
            if is_safe(n):
                n_queen(n + 1)

n_queen(0)
print(ans)


