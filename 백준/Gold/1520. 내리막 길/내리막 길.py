# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# M, N = map(int, input().split())
#
# graph = []
#
# for _ in range(M):
#     graph.append(list(map(int, input().split())))
#
# cnt = 0
# queue = deque()
# queue.append([0, 0])
#
#
# def BFS():
#     global cnt
#     while queue:
#         x, y = queue.popleft()
#         if x == M - 1 and y == N - 1:
#             cnt += 1
#
#         if y < N - 1:
#             if graph[x][y + 1] < graph[x][y]:
#                 queue.append([x, y + 1])
#         if y > 0:
#             if graph[x][y - 1] < graph[x][y]:
#                 queue.append([x, y - 1])
#         if x < M - 1:
#             if graph[x + 1][y] < graph[x][y]:
#                 queue.append([x + 1, y])
#         # 웨로도 간다는 표현은 없었는데..
#         if x > 0:
#             if graph[x - 1][y] < graph[x][y]:
#                 queue.append([x - 1, y])
#
#
#     # print(cnt)
# BFS()
# print(cnt)
# 시간 복잡도 터지는 풀이
# DP + DFS -> 시간 복잡도 줄이기
import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)] # dp[x][y]의 의미? x,y 좌표까지 갈 수 있는 경로 수

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x == M - 1 and y == N - 1:
        return 1

    # Memoization
    if dp[x][y] != -1:
        return dp[x][y]

    # 방문 처리
    dp[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] < graph[x][y]:
                # 다음 칸에서 목적지까지 가는 경로의 수를 현재 칸에 누적
                dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))