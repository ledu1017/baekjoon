import sys

def cutting(x, y, middle):
    global blue, white
    color = square[x][y]    # 분리된 사각형의 가장 왼쪽 위에 있는것을 기본 색으로 설정

    for i in range(x, x + middle):    # 행
        for j in range(y, y + middle):   # 열
            if color!= square[i][j]:    # 해당하는 행과 열이 모두 기본색이랑 같지 않을 경
                cutting(x, y, middle // 2)
                cutting(x + middle // 2, y, middle // 2)
                cutting(x, y + middle // 2, middle // 2)
                cutting(x + middle // 2, y + middle // 2, middle // 2)
                return
    
    if color == 1:
        blue += 1
    else:
        white += 1

if __name__ == "__main__":
    size = int(input())
    square = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]    # 사용자가 입력하는 사각형 색
    blue, white = 0, 0    # 1이면 blue, 0이면 white

    cutting(0, 0, size)
    print(white)
    print(blue)