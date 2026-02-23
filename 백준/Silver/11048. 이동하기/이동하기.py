import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
dp = [[0] * M for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int, input().split())))

dp[0][0] = graph[0][0]

for i in range(0, N):
    for j in range(0, M):
        if i == 0:
            dp[i][j] = graph[i][j] + dp[i][j - 1]
        elif j == 0:
            dp[i][j] = graph[i][j] + dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + graph[i][j]

print(dp[N - 1][M - 1])
