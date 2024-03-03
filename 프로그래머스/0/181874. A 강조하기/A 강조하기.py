def solution(myString):
    ans = ''
    for c in myString:
        if c == 'a':
            ans += 'A'
        elif c != 'A' and c.isupper():
            ans += c.lower()
        else:
            ans += c
            
    return ans
    
    "myString.lower().replace('a', 'A')"
    