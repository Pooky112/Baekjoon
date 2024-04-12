N= int(input())
ropes = [int(input()) for i in range(N)]

ropes.sort(reverse=True)

max_weight = max(ropes[i] * (i + 1) for i in range(N))

print(max_weight)