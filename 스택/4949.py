import sys

while True:
    sentence = sys.stdin.readline().rstrip()
    stack = ["."]    # 10번줄과 16번줄에서 에러 방지용 "."추가
    for w in sentence:
        if w == "(" or w == "[":
            stack.append(w)    # ( 또는 [가 있다면 stack리스트에 추가
        elif w == ")":
            if stack[-1] != "(":    # )가 나왔는데 stack 리스트에 (가 없다면
                stack.append(w)    # stack 리스트에 )만 추가하여 길이를 늘림
                break
            else:
                stack.pop()
        elif w == "]":
            if stack[-1] != "[":   # 10번줄과 동일
                stack.append(w)
                break
            else:
                stack.pop()

    if sentence == ".":    # .만 입력되었으면 종료
        break

    if len(stack)>1:    # stack 리스트의 길이가 처음 넣어두었던 .으로 인한 1 이상이라면 쌍으로 묶여 삭제되지 않았다는 뜻 
        print("no")
    else:
        print("yes")