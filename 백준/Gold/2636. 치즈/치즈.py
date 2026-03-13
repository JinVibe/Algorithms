import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]

melt_log = []
time = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    cnt = 0

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if board[nx][ny] == 0:
                    q.append((nx, ny))
                # 큐에 추가는 하지 않지만 0으로 바꿔줌으로서 더 이상 못 가게 함
                # 지워질 1들은 0과 붙어 있고 구멍인 부분들은 (0, 0)에서 시작하므로 건들지 않는다.
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    cnt += 1
                visited[nx][ny] = True

    melt_log.append(cnt)
    return cnt

while True:
    visited = [[False] * c for _ in range(r)]
    melt_cnt = bfs()

    if melt_cnt == 0:
        print(time)
        print(melt_log[-2])
        break
    time += 1