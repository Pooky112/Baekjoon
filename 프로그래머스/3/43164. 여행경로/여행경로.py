def solution(tickets):
    tickets.sort(reverse = True)
    answer = []
    routes = {}
    
    for start, end in tickets:
        if start in routes:
            routes[start].append(end)
        else:
            routes[start] = [end]
    
    def dfs(airport):
        while airport in routes and routes[airport]:
            next_airport = routes[airport].pop()
            dfs(next_airport)
        answer.append(airport)
    # stack = ["ICN"]
    # while stack:
    #     top = stack[-1]
    #     if top not in routes or len(routes[top]) == 0:
    #         answer.append(stack.pop())
    #     else:
    #         stack.append(routes[top].pop())
    dfs("ICN")
    return answer[::-1]