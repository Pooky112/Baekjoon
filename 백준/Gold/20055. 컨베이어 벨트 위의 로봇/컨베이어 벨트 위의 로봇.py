N, K = map(int, input().split())
A = list(map(int, input().split()))

def conveyor_belt_robot(N, K, A):
    step = 0
    robot = [False] * N
    
    while True:
        step += 1
        
        A = [A[-1]] + A[:-1]
        robot = [False] + robot[:-1]

        if robot[-1]:
            robot[-1] = False
        
        for i in range(N-2, -1, -1):
           if robot[i] and not robot[i+1] and A[i+1] > 0:
               robot[i] = False
               robot[i+1] = True
               A[i+1] -= 1

        if robot[-1]:
            robot[-1] = False
        
        if A[0]>0:
            robot[0] = True
            A[0] -= 1
            
        if A.count(0) >= K:
            return step
            
print(conveyor_belt_robot(N, K, A))
