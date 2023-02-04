'''
2023-02-04
백준 알고리즘 이진탐색 2805번
'''

def cutting_tree(tree_h, need_length):
    start_length = 0
    start_idx = 0
    end_idx = len(tree_h)-1
    end_length = tree_h[end_idx]

    while start_length <= end_length:
        result = 0
        middle_length = (start_length+end_length) // 2
        for i in tree_h:
            if i >= middle_length:
                result += i - middle_length
        if result == need_length:
            return middle_length
        elif result > need_length:
            start_length = middle_length + 1
        else:
            end_length = middle_length - 1
    return end_length

if __name__ == '__main__':
    total_tree_count, need_length = map(int, input().split())
    tree_h = list(map(int, input().split()))

    tree_h.sort()
    print(cutting_tree(tree_h, need_length))