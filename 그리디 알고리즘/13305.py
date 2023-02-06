def min_price(city, city_distance, oil_price):
    total_price = city_distance[0] * oil_price[0]    # 맨 처음 다음 도시로 가려면 첫번째 도시에서 무조건 기름을 넣어야함
    cheap_oil_price = oil_price[0]    # 가장 싼 기름을 첫번째 도시의 기름값으로 설정
    for i in range(1, city-1):
        if cheap_oil_price > oil_price[i]:    # 가장 싼 기름으로 설정한 가격이 다른 도시의 기름값보다 비쌀 때
            cheap_oil_price = oil_price[i]    # 가장 싼 기름값을 변경
            total_price += cheap_oil_price * city_distance[i]    # 가장 싼 기름 * 거리
        else:
            total_price += cheap_oil_price * city_distance[i]    # 가장 싼 기름가격 * 거리
    return total_price

if __name__ == '__main__':
    city = int(input())    # 도시 수
    city_distance = list(map(int, input().split()))    # 도시간의 거리
    oil_price = list(map(int, input().split()))    # 각 도시의 기름값

    print(min_price(city, city_distance, oil_price))