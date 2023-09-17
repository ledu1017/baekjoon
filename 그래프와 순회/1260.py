from collections import deque
import sys
read = sys.stdin.readline

n, m, v = map(int, read().split())    # n = 노드, m = 간선, v = 시작노드
graph = [[0] * (n+1) for _ in range(n+1)]    # 각 노드별로 어디로 이어져있는지 그래프
bfs_list = [0] * (n+1)    # bfs탐색을 할 때 방문한곳 표시
dfs_list = [0] * (n+1)    # dfs탐색을 할 때 방문한곳 표시

for _ in range(m):
    a,b = map(int, read().split())
    graph[a][b] = graph[b][a] = 1    # 각 노드별로 어디로 이어져 있는지 1로 표시

def bfs(v):    # 너비우선탐색
    q = deque()    # 시간복잡도 줄이기, 방문 순서대로 리스트에 추가될 예정
    q.append(v)    # 방문한곳을 리스트에 추가
    while q:
        v = q.popleft()    # 리스트의 제일 왼쪽부터 방문하기에 왼쪽거 빼기
        bfs_list[v] = 1    # 방문한곳은 1로 변환
        print(v, end = " ")    # 방문한곳 출력
        for i in range(1, n+1):
            if bfs_list[i] == 0 and graph[v][i] == 1:    # 방문하지 않았는데 간선이 연결되어 있다면
                q.append(i)    # 방문 예정이기에 리스트에 append
                bfs_list[i] = 1    # 방문 예정인곳은 순서대로 방문만 하면 되기에 방문한것으로 표시

def dfs(v):    # 깊이우선탐색
    dfs_list[v] = 1    # 방문한곳은 1로 변환
    print(v, end = " ")    # 방문한곳 출력
    for i in range(1, n + 1):
        if dfs_list[i] == 0 and graph[v][i] == 1:    # 방문하지 않았는데 간선이 연결되어 있다면
            dfs(i)    # 재귀로 반복

dfs(v)
print()
bfs(v)