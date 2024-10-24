import sys

n = int(sys.stdin.readline())
commands = []
for i in range(n):
    commands.append(sys.stdin.readline().strip())
stack = []
result = []
for i in range(0, n):
    command = commands[i]

    if command.startswith("push"):
        _, x = command.split(" ")
        stack.append(int(x))
    elif command == "pop":
        if stack:
            result.append(stack.pop())
        else:
            result.append(-1)
    elif command == "size":
        result.append(len(stack))
    elif command == "empty":
        result.append(0 if stack else 1)
    elif command == "top":
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

print("\n".join(map(str, result)) + "\n")

