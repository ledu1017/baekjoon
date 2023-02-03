n, k = map(int, input().split())

coin = []

def coin_value(n):
    for _ in range(n):
        coin.append(int(input()))

def coin_result(k):
    count = 0
    i = len(coin)-1

    while k != 0:
        if k - coin[i] >= 0:
            count += k // coin[i]
            k = k % coin[i]
        else:
            i -= 1
    return count

coin_value(n)
print(coin_result(k))