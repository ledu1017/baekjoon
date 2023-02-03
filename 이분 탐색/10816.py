import re

def card_count(input_num_A, input_num_B, card_dict):
    for i in input_num_A:
        start = 0
        end = len(input_num_B) - 1
        while start <= end:
            middle = (start+end) // 2
            if input_num_B[middle] == i:
                card_dict[i] += 1
                break
            elif input_num_B[middle] > i:
                end = middle -1
            else:
                start = middle + 1

    return card_dict

if __name__ == '__main__':
    card_dict = {}
    input_count_A = input()
    input_num_A = list(map(int, input().split()))
    input_count_B = input()
    input_num_B = list(map(int, input().split()))
    a = input_num_B.copy()
    input_num_B.sort()

    for i in input_num_B:
        card_dict[i] = 0
    card_dict = card_count(input_num_A, input_num_B, card_dict)
    #for key, value in card_dict.items():
    #    print(value, end=' ')

    for i in a:
        print(card_dict[i], end=' ')