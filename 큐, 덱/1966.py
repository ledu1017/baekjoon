import sys

size = int(input())
result = []

for _ in range(size):
    count = 1
    quantity, index = map(int, sys.stdin.readline().split())
    importance_list = list(map(int, sys.stdin.readline().split()))    # 중요도가 저장되어 있는 리스트
    index_list = [0 for _ in range(quantity)]    # 사용자가 원하는 인덱스 위치는 1, 나머지는 0
    index_list[index] = 1

    while True:
        max_num = max(importance_list)
        if index_list[0] == 1 and importance_list[0] == max_num:    # 가장 큰 중요도이고 사용자가 원하는 인덱스 위치였을 때
            result.append(count)
            break
        elif index_list[0] == 0 and importance_list[0] == max_num:    # 가장 큰 중요도지만 사용자가 원하는 인덱스 위치는 아닐때
            importance_list.pop(0)
            index_list.pop(0)
            count+=1
        else:    # 가장 큰 중요도가 아닐때
            importance_list.append(importance_list[0])    # 해당 값을 가장 뒤로 추가
            importance_list.pop(0)    # 해당 리스트의 첫번째값 삭제
            index_list.append(index_list[0])    # 해당 값을 가장 뒤로 추가
            index_list.pop(0)    # 해당 리스트의 첫번째값 삭제

for i in result:
    print(i)