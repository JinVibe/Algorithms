import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n + 1):
    graph[i].sort()

visited = [False for _ in range(n + 1)]
answer = [-1 for _ in range(n + 1)]


def bfs(graph, r):
    queue = deque()
    depth = 0

    queue.append((r, depth))
    visited[r] = True
    answer[r] = depth

    while queue:
        current_vertex, depth = queue.popleft()
        answer[current_vertex] = depth

        for next_vertex in graph[current_vertex]:
            if not visited[next_vertex]:
                queue.append((next_vertex, depth + 1))
                visited[next_vertex] = True


bfs(graph, r)

for x in answer[1::]:
    print(x)