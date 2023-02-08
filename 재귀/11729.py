num = int(input())

def hanoi(num, start, end):
    if num > 1:
        # 하노이탑 이동 알고리즘에 따라 숫자를 왼쪽에서 오른쪽으로 옮길 때 사용
        # 6-start-end를 하면 이동해야 하는 막대의 위치를 알 수 있음
        hanoi(num-1, start, 6-start-end)
    print(start,end)
    if num >1 :
        # 하노이탑 이동 알고리즘에 따라 숫자를 오른쪽에서 왼쪽으로 옮길 때 사용
        hanoi(num-1, 6-start-end, end)

print(2**num-1)
hanoi(num, 1, 3)