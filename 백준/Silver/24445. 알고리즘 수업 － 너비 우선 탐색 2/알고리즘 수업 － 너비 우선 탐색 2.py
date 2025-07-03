from collections import deque
import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
edge = [[] for _ in range(n+1)]
visited = [0] * (n+1)
visited[r] = 1
cnt = 1
queue = deque([r])

for _ in range(m):
    a,b = map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)

for i in range(1,n+1):
    edge[i].sort(reverse = True)

while queue:
    v = queue.popleft()
    for i in edge[v]:
        if visited[i]:
            continue
        cnt+=1
        visited[i] = cnt
        queue.append(i)

print(*visited[1:], sep="\n")