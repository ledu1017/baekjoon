import sys

def zip_file(x, y, middle):
    color = square[x][y]
    for i in range(x, x+middle):
        for j in range(y, y+middle):
            if color != square[i][j]:
                print("(", end='')
                zip_file(x, y, middle // 2)
                zip_file(x, y + middle // 2, middle // 2)
                zip_file(x + middle // 2, y, middle // 2)
                zip_file(x + middle // 2, y + middle // 2, middle // 2)
                print(")", end='')
                return

    if color == 1:
        print("1", end='')
        return
    else:
        print("0",end='')
        return

if __name__ == "__main__":
    size = int(input())
    square = [list(map(int, sys.stdin.readline().strip())) for _ in range(size)]

    zip_file(0, 0, size)