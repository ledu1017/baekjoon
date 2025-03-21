def cal(data):
    if sum(data) == 180:
        if data[0] == data[1] == data[2]:
            return "Equilateral"
        elif data[0] == data[1] or data[1] == data[2] or data[0] == data[2]:
            return "Isosceles"
        else:
            return "Scalene"
    else:
        return "Error"

data = list(int(input()) for i in range(3))

print(cal(data))