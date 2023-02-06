p_num=int(input())    # 사람 수
t_time=0    # 시간의 최소 합

p_time=list(map(int,input().split()))    # 각 사람이 돈을 인출하는데 걸리는 시간
p_time.sort()    # 시간이 짧은 순으로 오름차순 정렬

for i in range(p_num):    # 사람 수 만큼 반복
  num=p_time[i]*(p_num-i)
  t_time+=num
  
print(t_time)