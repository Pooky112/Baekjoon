S = input()

answer = ''
alphabet = []
for i in range(26):
    alphabet.append(chr(ord('A')+i))

for s in S:
    if s.isupper():
        answer += alphabet[(ord(s) + 13 - ord('A')) % 26]
    elif s.islower():
        answer += alphabet[(ord(s) + 13 - ord('a')) % 26].lower()
    else:
        answer += s

print(answer)

