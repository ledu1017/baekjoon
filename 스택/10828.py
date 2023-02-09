import sys
size = int(input())
stack = []

for _ in range(size):
    order = sys.stdin.readline().split()    # 빠르게 입력을 받을 수 있음

    if order[0] == "push":
        stack.append(order[1])
    elif order[0] == "pop":
        if stack:
            print(stack.pop(-1))    # 마지막 인덱스에 있는 값을 출력하고 삭제
        else:
            print("-1")
    elif order[0] == "size":
        print(len(stack))
    elif order[0] == "empty":
        if stack:
            print("0")
        else:
            print("1")
    elif order[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print("-1")
