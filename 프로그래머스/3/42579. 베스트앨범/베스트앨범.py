def solution(genres, plays):
    answer = []
    total = {}
    music_table = {}
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in total:
            total[g] = p
            music_table[g] = [(p, i)]
        else:
            total[g] += p
            music_table[g].append((p, i))
    
    for g in music_table:
        music_table[g].sort(key = lambda x: (-x[0], x[1]))
    
    for g, _ in sorted(total.items(), key = lambda x: x[1], reverse=True):
        print(music_table[g][:2])
        answer.extend([song[1] for song in music_table[g][:2]])
        
    return answer
    
