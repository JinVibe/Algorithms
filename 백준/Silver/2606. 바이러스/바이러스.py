# 연결
import sys

input = sys.stdin.readline


def dfs(v): # 기본 형태는 항상 그래왔듯 외우면 됩니다. + visited와 graph라는 변수도 같이 말이죠
    visited[v] = True
    for ele in graph[v]:
        if not visited[ele]:
            dfs(ele)


num = int(input())

n = int(input())
visited = [False] * (num + 1)
graph = [[] for _ in range(num + 1)]

for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = True

dfs(1)

print(visited.count(True) - 1)
