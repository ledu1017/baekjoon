from collections import deque

size = int(input())
card_list = deque(range(1,size+1))

while len(card_list) != 1:
    card_list.popleft()    # 가장 처음꺼 제거
    card_list.append(card_list[0])    # 두번째에 있던 숫자 마지막에 추가
    card_list.popleft()    # 두번째에 있던 숫자 제거

print(card_list.pop())