x, y, w, h = map(int, input().split())
print(min(x,y, w-x, h-y))    # 각 x,y축으로 가는게 작은지 아니면 w와 h로 가는게 작은지