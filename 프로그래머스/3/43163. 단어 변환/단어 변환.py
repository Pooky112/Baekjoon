from collections import deque

def is_different(curr, word):
    return sum(a != b for a, b in zip(curr,word)) == 1

def solution(begin, target, words):
    answer = 0
    visited = []
    
    if target not in words:
        return 0
    #bfs
    queue = deque([(begin, 0)])
    
    
    while queue:
        curr, count = queue.popleft()
        if curr == target:
            return count
        for word in words:
            if word not in visited and is_different(curr, word):
                visited.append(word)
                queue.append((word, count + 1))
    
    return 0