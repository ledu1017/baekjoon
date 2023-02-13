import sys
from collections import deque

quantity = int(input())
result = []

for _ in range(quantity):
    check = 0
    count = 0
    user_function = sys.stdin.readline().strip()
    list_size = int(sys.stdin.readline().strip())
    list_num = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    # 입력 한번에 결과 한번씩 출력 성공
    if list_size == 0:
        list_num = []

    for function in user_function:    # 사용자가 입력한 함수 하나씩 읽기
        if function == "R":    # 뒤집는건 R 나온 횟수를 세어두고 홀수만큼 나왔으면 뒤집고 아니면 안뒤집고
            count += 1
        elif function == "D":    # D일땐 삭제
            if len(list_num) == 0:    # 아무것도 없는데 삭제하라고 하면 error 출력
                print("error")
                break
            else:
                if count % 2 == 0:    # 짝수번 뒤집으면 원래대로라서 왼쪽에서 삭제
                    list_num.popleft()
                else:    # 한번 뒤집은거로 치고 뒤에서 삭제
                    list_num.pop()

    else:
        if count % 2 == 0:    # 짝수번 뒤집었으면 원래대로 출력
            print("[" + ",".join(list_num) + "]")
        else:    # 홀수번 뒤집었으면 뒤집어주기
            list_num.reverse()
            print("[" + ",".join(list_num) + "]")
        
'''
    # 결과 한번에 출력, 시간초과 발생
    for function in user_function:
        if function == "R":
            count += 1

        if '' not in list_num:
            try:
                if function == "D":
                    if count % 2 == 0:
                        list_num.popleft()
                    else:
                        list_num.pop()
            except:
                result.append("error")
                check = 1
                break
        else:
            if function == "D":
                result.append("error")
            elif function == "R":
                result.append("")
            check = 1
            break

    if check == 0:
        if count % 2 == 0:
            result.append(list_num)
        else:
            result.append(list(reversed(list_num)))

for i in range(len(result)):
    if result[i] == "error":
        print(result[i])
    else:
        print("[" + ",".join(result[i]) + "]")
'''