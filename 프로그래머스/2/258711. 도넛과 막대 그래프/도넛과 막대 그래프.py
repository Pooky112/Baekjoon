from collections import defaultdict

def solution(edges):
    answer = [0] * 4
    visited = []
    
    route_out = defaultdict(list)
    route_in = defaultdict(list)
    
    for start, end in edges:
        route_out[start].append(end)
        route_in[end].append(start)
    
    nodes = set(list(route_in.keys()) + list(route_out.keys()))
    
    for node in nodes:
        #나가는 노드의 수가 총 그래프 종류의 수 일 때
        if len(route_out[node]) >= 2  and len(route_in[node]) == 0:
            answer[0] = node
        elif len(route_out[node]) == 0 and len(route_in[node]) >= 1:
            answer[2] += 1
        elif len(route_out[node]) == 2 and len(route_in[node]) >= 2:
            answer[3] += 1
        
        
    answer[1] = len(route_out[answer[0]]) - answer[3] - answer[2]
    
    return answer
        