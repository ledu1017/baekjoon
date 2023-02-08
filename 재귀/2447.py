size = int(input())

def star_shape(size):
    if size == 1:    # N일때의 모양은 N-1일때의 모양 N-1의 모양은 N-2의 모양....들이 모인것들이기에 가장 작은 모양부터 만들기 위함
        return "*"    # 가장 작을때는 * 하나로 모양을 만들기 때문
    Stars = star_shape(size//3)     # 가장 작은모양을 만들기 위해 가장 작아질때까지 재귀로 반복
    L = []    # 모양이 저장 될 공간

    for star in Stars:
        L.append(star*3)    # 가운데에만 구멍뚫린 모양이기에 여기는 다 채움
    for star in Stars:
        L.append(star + " "*(size//3) + star)    # 가운데에 구멍을 만들기위해 가운데에 빈칸을 추가
    for star in Stars:
        L.append(star*3)    # 가운데에만 구멍뚫린 모양이기에 여기는 다 채움

    return L    # 모양이 저장되어있는 L을 반환

print("\n".join(star_shape(size)))    # 리스트에 저장되어 있고, 마지막은 \n으로 되어있기에 \n을 제거하면서 합치기