from itertools import permutations

def solution(k, dungeons):
    max_count = 0
    for order in permutations(dungeons, len(dungeons)):
        cur = k
        count = 0
        for min_req, consumed in order:
            if cur >= min_req:
                cur -= consumed
                count += 1
            else:
                break
        max_count = max(max_count, count)
    
    return max_count

#solution = lambda k, d: max([solution(k-u, d[:i] + d[i+1:]) +1 for i, (m, u) in enumerate(d) if k>= m] or [0])