import sys

def cutting(x, y, middle):
    global one, zero, minus
    number = square[x][y]
    for i in range(x, x+middle):
        for j in range(y, y+middle):
            if number != square[i][j]:
                cutting(x, y, middle // 3)
                cutting(x, y + middle // 3, middle // 3)
                cutting(x, y + middle // 3 * 2, middle // 3)
                cutting(x + middle // 3, y, middle // 3)
                cutting(x + middle // 3, y + middle // 3, middle // 3)
                cutting(x + middle // 3, y + middle // 3 * 2, middle // 3)
                cutting(x + middle // 3 * 2, y, middle // 3)
                cutting(x + middle // 3 * 2, y + middle // 3, middle // 3)
                cutting(x + middle // 3 * 2, y + middle // 3 * 2, middle // 3)
                return

    if number == -1:
        minus += 1
    elif number == 0:
        zero += 1
    else:
        one += 1
    
if __name__ == "__main__":
    size = int(input())
    square = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]
    one, zero, minus = 0, 0, 0
    cutting(0, 0, size)

    print(minus, zero, one)