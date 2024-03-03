def solution(todo_list, finished):
    ans = []
    for todo, check in zip(todo_list, finished):
        if not check:
            ans.append(todo)
    return ans
    