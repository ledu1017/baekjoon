# 해결 못함 회의실 배정
user_input = list(input())
plus_result = []
minus_result = []

def split_sent(user_input):
    count = 0
    for i in range(len(user_input)):
        if user_input[i] == '-':
            for j in range(i+1, len(user_input)):
                if user_input[j] != '-':
                    minus_result.append(user_input[j])
                else:
                    break
                count = j
        else:
            if count == len(user_input)-1:
                return 0
            plus_result.append(user_input[count])
            count += 1

#print(split_sent(user_input))
split_sent(user_input)
print(minus_result)
print(plus_result)