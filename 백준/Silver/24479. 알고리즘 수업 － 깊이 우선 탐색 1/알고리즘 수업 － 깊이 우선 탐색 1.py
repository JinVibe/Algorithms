import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

def dfs(t):
    global cnt
    visited[t] = cnt
    edges[t].sort() # 왜 정렬 -> 무조건 작은 수에서 큰 수로 경로 정렬
    for j in edges[t]:
        if visited[j] == 0: # 미방문 시
            cnt += 1
            dfs(j)


n, m, r = map(int, input().split())
edges = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

dfs(r)

for i in range(1, n + 1):
    print(visited[i])