size = int(input())
stack = []

for _ in range(size):
    money = int(input())
    if money == 0:
        del stack[-1]    # 0입력시 가장 마지막 숫자 지우기
    else:
        stack.append(money)    # 0이외의 숫자라면 추가하기

print(sum(stack))    # 리스트에 있는 숫자들 합