from collections import deque

size, pop_size = map(int, input().split())
index = deque(map(int, input().split()))

num_list = deque([i for i in range(1, size+1)])

option = 0
count = 0
idx = 0
result = []

while len(result) != pop_size:
    for i in range(int(len(num_list)//2)):
        if (num_list[i] == index[0]    # 찾는 인덱스가 가운데에 있거나 그 왼쪽에 있다면 왼쪽에서 빼나가는게 빠름
            or num_list[int(len(num_list)//2)] == index[0]):
            option = 1
            break
    
    if num_list[0] == index[0]:    # 가장 앞에있는 수가 원하는 인덱스에 있는 수일 때
        result.append(num_list.popleft())    # result라는 리스트에
        index.popleft()
        option = 0
        continue

    if option == 1:    # 왼쪽 숫자를 하나 빼서 뒤로 보내는 방식으로 원하는 인덱스를 찾는게 빠를 때
        count += 1
        num_list.append(num_list[0])
        num_list.popleft()
        option = 0
    else:    # 오른쪽 숫자를 하나 빼서 앞으로 보내는 방식으로 원하는 인덱스를 찾는게 빠를 때
        count += 1
        num_list.appendleft(num_list[-1])
        num_list.pop()
        option = 0

print(count)