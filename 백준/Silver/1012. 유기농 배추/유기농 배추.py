import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

T = int(input())

def dfs(x, y):
    if x <= -1 or x >= M or y <= -1 or y >= N:
        return False
    if matrix[y][x] == 1:
        matrix[y][x] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1
    cnt = 0
    for i in range(M):
        for j in range(N):
            if dfs(i, j):
                cnt += 1

    print(cnt)
