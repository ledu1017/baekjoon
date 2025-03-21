def cal(point):
    x_min = point[0][0]
    y_min = point[0][1]
    x_max = point[0][0]
    y_max = point[0][1]
    for i in range(len(point)):
        if x_min > point[i][0]:
            x_min = point[i][0]
        if y_min > point[i][1]:
            y_min = point[i][1]
        if x_max < point[i][0]:
            x_max = point[i][0]
        if y_max < point[i][1]:
            y_max = point[i][1]

    return (x_max - x_min) * (y_max - y_min)

point = []
count = int(input())
for i in range(count):
    point.append(list(map(int, input().split())))

print(cal(point))