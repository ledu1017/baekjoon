while True:
    length = list(map(int, input().split()))
    c = max(length)
    hap = 0

    if length[0] == 0 and length[1] == 0 and length[2] == 0:
        break

    for i in range(len(length)):
        if length[i] != c:    # 가장 긴 길이를 제외한 나머지
            hap += length[i]**2    # 제곱해서 더해주기

    if hap == c**2:    # a^2 + b^2 == c^2이면 직삼각
        print("right")
    else:
        print("wrong")