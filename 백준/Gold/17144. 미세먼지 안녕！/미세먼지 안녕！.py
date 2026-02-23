# import sys
#
# input = sys.stdin.readline
#
# R, C, T = map(int, input().split())
#
# A = []
# tmp = [[] * C for _ in range(R)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# for _ in range(R):
#     A.append(list(map(int, input().split())))
#
#
# def cycle():
#     pass
#
#
# for i in range(R):
#     for j in range(C):
#         dirs = [0, 1, 2, 3]
#         if A[i][j] > 0:
#             if i == 0 or A[i - 1][j] == -1:
#                 dirs.remove(0)
#             if i == R - 1 or A[i + 1][j] == -1:
#                 dirs.remove(1)
#             if j == 0 or A[i][j - 1] == -1:
#                 dirs.remove(2)
#             if j == C - 1 or A[i][j + 1] == -1:
#                 dirs.remove(3)
#
#         for d in dirs:
#             A[i + dx[d]][j + dy[d]] += A[i][j] // 5
#
#         A[i][j] -= len(dirs) * (A[i][j] // 5)
#
# print(*A, sep="\n")

import sys

input = sys.stdin.readline

R, C, T = map(int, input().split())

A = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(R):
    A.append(list(map(int, input().split())))

for i in range(R):
    for j in range(C):
        if A[i][j] == -1:
            x, y = i, j  # 공기청정기의 아랫부분이 저장
            break


def cycle():
    global A
    new_A = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if A[r][c] == -1:
                new_A[r][c] = -1
                continue
            if A[r][c] > 0:
                cnt = 0
                for d in range(4):
                    nr = r + dx[d]
                    nc = c + dy[d]
                    if 0 <= nr < R and 0 <= nc < C and A[nr][nc] != -1:
                        new_A[nr][nc] += A[r][c] // 5
                        cnt += 1
                new_A[r][c] += (A[r][c] - cnt * (A[r][c] // 5))

    A = new_A

    # 윗 사각형
    for i in range(x - 1 - 1, 0, -1):
        A[i][0] = A[i - 1][0]
    for i in range(C - 1):
        A[0][i] = A[0][i + 1]
    for i in range(x - 1):  # x - 1
        A[i][C - 1] = A[i + 1][C - 1]
    for i in range(C - 1 - 1, 0, -1):
        A[x - 1][i + 1] = A[x - 1][i]

    # 아래 사각형
    for i in range(x + 1, R - 1):
        A[i][0] = A[i + 1][0]
    for i in range(0, C - 1):
        A[R - 1][i] = A[R - 1][i + 1]
    for i in range(R - 1 - 1, x - 1, -1):
        A[i + 1][C - 1] = A[i][C - 1]
    for i in range(C - 1 - 1, 0, -1):
        A[x][i + 1] = A[x][i]

    A[x - 1][1] = 0
    A[x - 1][0] = -1
    A[x][1] = 0
    A[x][0] = -1


for _ in range(T):
    cycle()

ans = 0

for i in range(R):
    ans += sum(A[i])

print(ans + 2)  # -1 2개 더 해주기
