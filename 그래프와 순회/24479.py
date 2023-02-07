import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)    # 각 번호의 노드가 갈 수 있는 노드 정해주기
    graph[b].append(a)

def dfs(v):
    global count
    visited[v] = count    # 해당 노드를 몇번째에 방문했는지 카운트
    graph[v].sort()    # 각 번호의 노드가 갈 수 있는 노드 오름차순으로 정렬
    for g in graph[v]:
        if visited[g] == 0:    # 방문 안했던 노드라면
            count += 1    # 방문순서 +1
            dfs(g)    # 방문 안했던 노드로 다시 반복

dfs(r)

for i in range(1, n + 1):
    print(visited[i])