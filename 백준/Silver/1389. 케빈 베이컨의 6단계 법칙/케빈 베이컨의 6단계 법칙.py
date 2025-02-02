from _collections import deque


def bfs(start):
    queue = deque()
    queue.append(start)

    num = [0] * (n + 1)
    visited = [start]

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if i not in visited:
                num[i] = num[x] + 1
                visited.append(i)
                queue.append(i)

    return sum(num)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

res = []

for i in range(1, n + 1):
    res.append(bfs(i))

print(res.index(min(res)) + 1)
