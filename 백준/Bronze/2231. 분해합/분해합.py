
def solution(N):
    for i in range(1, N+1):
        length = len(str(i))
        num = i
        for j in range(length):
            num += int(str(i)[j])
        if num == N:
            return i

    return 0

N = int(input())
print(solution(N))