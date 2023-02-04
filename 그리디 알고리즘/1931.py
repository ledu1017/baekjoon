'''
2023-02-04
백준 알고리즘 그리디 알고리즘 1931번
회의실 배정
'''
def meeting(meeting_num, meeting_time):
    count = 1    # 진행한 회의 수
    end_time = meeting_time[0][1]    # 회의 시간 리스트에서 첫번째 회의의 끝나는 시간

    for i in range(1, meeting_num):
        if meeting_time[i][0] >= end_time:    # 회의 끝나는 시간이 다음 회의 시작시간보다 작을때
            end_time = meeting_time[i][1]    # 회의 끝나는 시간은 이전 회의의 끝나는 시간
            count += 1    # 진행한 회의 수 +1
    return count

if __name__ == '__main__':
    meeting_num = int(input())    # 회의 갯수
    meeting_time = []    # 회의 일정 리스트
    for i in range(meeting_num):
        meeting_time.append(list(map(int, input().split())))

    '''
    두번 정렬하는 이유는 1 2, 2 2 일경우 회의 수가 2가 나오지만
    2 2, 1 2로 끝나는 시간만 정렬 될 경우 회의 수가 1이 나온다
    '''
    meeting_time.sort()    # 회의 시작시간 기준 오름차순 정렬
    meeting_time.sort(key = lambda x:(x[1], x[0]))    # 회의 끝나는 시간 기준 오름차순 정렬
    print(meeting(meeting_num, meeting_time))
