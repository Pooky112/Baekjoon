def find(v_set, x):
    if v_set[x] != x:
        v_set[x] = find(v_set, v_set[x])
    return v_set[x]

def union(v_set, a, b):
    a = find(v_set, a)
    b = find(v_set, b)
    if a < b:
        v_set[b] = a
    else:
        v_set[a] = b

def solution(n, costs):
    answer = 0
    
    costs.sort(key = lambda x: x[2])
    v_set = [i for i in range(n)]
    
    for cost in costs:
        a, b, c = cost
        if find(v_set, a) != find(v_set, b):
            union(v_set, a, b)
            answer += c
    
    
    return answer