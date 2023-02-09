import sys

size = int(input())
for _ in range(size):
    stack = []
    shape = sys.stdin.readline().strip()    # 빠르게 입력받고 마지막 개행문자 제거
    for detail_shape in shape:
        if detail_shape == "(":
            stack.append(detail_shape)    # (모양만 리스트에 추가
        elif detail_shape == ")":
            if stack:    # 리스트에 있는 내용은 '('만 있기 때문에 ')'가 나오면 짝지어서 없애주기 위함
                stack.pop()    # 리스트 하나 제거
            else:
                stack.append(detail_shape)    # )모양 추가해서 리스트를 비어있는 상태가 안되게 만들기
                break
    if stack:    # 리스트에 내용이 있다는것은 짝지어져 없어지지 않았다는 의미
        print("NO")
    else:
        print("YES")