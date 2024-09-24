import sys

def find_least_gori(N, K):
    K.sort()
    chain = 0
    gori = 0
    for k in K:
        if k == N - 1:
            return gori + k
        elif k > N - 1:
            return gori + N - 1
        else:
            N -= (k + 1)
            gori += k

    return chain


N = int(sys.stdin.readline())
K = list(map(int, sys.stdin.readline().split()))

print(find_least_gori(N,K))
        
