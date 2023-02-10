import sys
from collections import deque    # 큐, 스택에 사용하기에 용이함

size = int(input())
queue = deque()

for _ in range(size):
    order = sys.stdin.readline().split()
    
    if order[0] == "push":
        queue.appendleft(order[1])    # queue 리스트의 왼쪽에 새로운 숫자를 삽입
    elif order[0] == "pop":
        if queue:
            print(queue.pop())
        else:
            print("-1")
    elif order[0] == "size":
        print(len(queue))
    elif order [0] == "empty":
        if queue:
            print("0")
        else:
            print("1")
    elif order[0] == "front":
        if queue:
            print(queue[-1])
        else:
            print("-1")
    elif order[0] == "back":
        if queue:
            print(queue[0])
        else:
            print("-1")
