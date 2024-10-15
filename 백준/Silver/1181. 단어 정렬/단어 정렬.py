import sys

N = int(sys.stdin.readline())
words = set()
count = {}

for i in range(N):
    words.add(sys.stdin.readline().strip())

sorted_words = sorted(words, key = lambda x: (len(x), x))

for word in sorted_words:
    print(word)