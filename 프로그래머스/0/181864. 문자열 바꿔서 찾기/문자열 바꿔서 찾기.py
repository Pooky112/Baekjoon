def solution(myString, pat):
    changed = ''
    for c in myString:
        if c == "A":
            changed += "B"
        elif c == "B":
            changed += "A"
    
    return 1 if pat in changed else 0

"return int(pat in myString.replace('A', 'C').replace('B', 'A').replace('C', 'B'))"