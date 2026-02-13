import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
Hx, Hy = map(int, input().split())  # 시작점
Ex, Ey = map(int, input().split())  # 끝점

Hx -= 1
Hy -= 1
Ex -= 1
Ey -= 1

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))


def bfs(r, c):
    queue = deque([(r, c, 0, 1)]) # r, c 위치에서 item 들고 시작
    visited = [[[False] *  2 for _ in range(M)] for _ in range(N)]
    visited[r][c][0] = True
    while queue:
        r, c, cnt, item = queue.popleft()
        if r == Ex and c == Ey: return cnt
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc][item]: continue # 지나갔던 곳은 skip
                if graph[nr][nc] == 1 and item == 1: # item 가졌는데 벽인 1에 갔다면?
                    visited[nr][nc][1] = True
                    queue.append((nr, nc, cnt + 1, item - 1))
                elif graph[nr][nc] == 0: # 길인 0으로 감
                    visited[nr][nc][item] = True
                    queue.append((nr, nc, cnt + 1, item))

    return -1

print(bfs(Hx, Hy))
