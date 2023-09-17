from collections import deque
import sys
read = sys.stdin.readline

n, m, v = map(int, read().split())    # 노드, 간선, 시작노드 입력
graph = [[] for _ in range(n+1)]    # 입력된 노드와 간선의 관계로 만들어질 그래프
bfs_list = [0] * (n+1)    # 어느 노드에 몇번째에 방문했는지 저장

for _ in range(m):    # 그래프 그리기 위해 노드와 간선의 관계 연결
    a, b = map(int, read().split())    # 연결 내용 입력
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1): # 인접노드 정보 오름차순 정렬
    graph[i].sort()

def bfs(v):
    count = 1
    q = deque([v])    # 방문 노드를 q deque리스트에 추가
    bfs_list[v] = count    # bfs_list의 v번째는 노드를 의미하고 해당 노드를 몇번째에 방문했는지 저장
    while q:
        v = q.popleft()    # q에는 방문 예정인 노드들이 들어있음. 그래서 왼쪽에서부터 방문
        for i in graph[v]:    # 
            if bfs_list[i] == 0:    # 아직 해당노드에 방문하지 않았다면
                q.append(i)    # 방문 예정이기에 q에 추가
                count += 1    # 몇번째에 방문인지 알기 위해서 count를 사용
                bfs_list[i] = count    # 방문한 곳 몇번째인지 저장
    
    for i in bfs_list[1:]:
        print(i)

bfs(v)