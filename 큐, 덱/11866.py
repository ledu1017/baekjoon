from collections import deque

size, del_num = map(int, input().split())
list = deque(range(1,size+1))
result = []

while list:
    for i in range(del_num-1):
        list.append(list.popleft())   # 번호가 다 없어질때까지 돌려야 하기 때문에 지워야 할 번호 빼고는 뒤로 보냄
    result.append(list.popleft())    # 지워야 할 번호는 list에서 지우고 result에 삽입

print("<", end='')
print(', '.join(map(str, result)), end='')
print(">")