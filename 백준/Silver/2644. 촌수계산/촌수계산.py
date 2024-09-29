def dfs(v, goal, depth):
    visited[v] = 1
    if v == goal:
        print(depth)
        exit(0)

    for ele in relations[v]:
        if not visited[ele]:
            dfs(ele, goal, depth + 1)

n = int(input())
a, b = map(int, input().split())
m = int(input())
relations = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    relations[x].append(y)
    relations[y].append(x)

visited = [0] * (n + 1)

dfs(a, b, 0)

print(-1)
