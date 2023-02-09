import sys

size = int(sys.stdin.readline().strip())
stack = []
list = []
i = 1
pop_push = []
for _ in range(size):
    stack.append(int(sys.stdin.readline().strip()))

while stack:
    if not list:
        pop_push.append("+")
        list.append(i)
        i+=1
    else:
        if list[-1] == stack[0]:
            pop_push.append("-")
            list.pop()
            stack.pop(0)
        elif list[-1] > stack[0]:
            pop_push.append("NO")
            break
        else:
            pop_push.append("+")
            list.append(i)
            i+=1

if pop_push[-1] != "NO":
    print(*pop_push, sep='\n')
else:
    print("NO")