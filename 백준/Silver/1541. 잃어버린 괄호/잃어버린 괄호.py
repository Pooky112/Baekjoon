import sys

expression = sys.stdin.readline().strip().split("-")

for i in range(len(expression)):
    if "+" in expression[i]:
        temp = list(map(int, expression[i].split("+")))
        expression[i] = sum(temp)
    else:
        expression[i] = int(expression[i])



answer = expression[0]
for i in range(1, len(expression)):
    answer -= expression[i]

print(answer)