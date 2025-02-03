import sys
from collections import deque

input = sys.stdin.readline

def bfs(s):
    queue = deque([s])
    visited[s] = 1
    cnt = 2

    while queue:
        s = queue.popleft()

        for ele in graph[s]:
            if visited[ele] == 0:
                queue.append(ele)
                visited[ele] = cnt
                cnt += 1


n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()

bfs(r)

for i in visited[1::]:
    print(i)
