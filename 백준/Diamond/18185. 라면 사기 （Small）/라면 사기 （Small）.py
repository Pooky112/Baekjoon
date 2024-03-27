n = int(input())
arr = list(map(int, input().split())) + [0, 0]

cost = 0
for i in range(n):
  if arr[i+1] > arr[i+2]:
    pack = min(arr[i], arr[i+1] - arr[i+2])
    arr[i] -= pack
    arr[i+1] -= pack
    cost += 5 * pack
    
    pack = min(arr[i], arr[i+1], arr[i+2])
    arr[i] -= pack
    arr[i+1] -= pack
    arr[i+2] -= pack
    cost += 7 * pack

  else:
    pack = min(arr[i], arr[i+1], arr[i+2])

    arr[i] -= pack
    arr[i+1] -= pack
    arr[i+2] -= pack
    cost += 7 * pack
    
    pack = min(arr[i], arr[i+1])
    
    arr[i] -= pack
    arr[i+1] -= pack
    cost += 5 * pack
    

  cost += arr[i] * 3
  arr[i] = 0

print(cost)