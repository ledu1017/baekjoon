def search_B_in_A(input_num_A, input_num_B):
    for i in input_num_B:
        start = 0    # 시작 인덱스
        end = len(input_num_A) - 1    # 마지막 인덱스
        while start <= end:
            middle = (start+end) // 2    # 이분탐색을 위해 시작과 끝 사이의 인덱스 찾기
            if input_num_A[middle] == i:    # 가운데 값이 찾는 값과 같다면 1출력
                print("1")
                break
            elif input_num_A[middle] > i:    # 가운데 값이 찾는 값보다 크다면
                end = middle - 1    # 끝을 가운데에서 -1한 값을 end에 삽입
            else:    # 가운데 값이 찾는 값보다 작다면
                start = middle + 1    # 시작을 가운데에서 +1한 값을 start에 삽입
        if(start > end):
            print("0")


if __name__ =="__main__":
    input_count_A = int(input())
    input_num_A = list(map(int, input().split()))    # 입력받은 수 정수형으로 스페이스바로 구분하여 리스트 삽입
    input_num_A.sort()    # 이분탐색을 위해 오름차순 정렬
    input_count_B = int(input())
    input_num_B = list(map(int, input().split()))    # 입력받은 수 정수형으로 스페이스바로 구분하여 리스트 삽입

    search_B_in_A(input_num_A, input_num_B)
