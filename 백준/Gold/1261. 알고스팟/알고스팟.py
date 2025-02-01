from _collections import deque


def bfs(a, b):
    queue = deque()
    queue.append([a, b]) # 초기 값 넣기
    dist[0][0] = 0 # 첫 벽 깬 횟수 초기화

    while queue:
        x, y = queue.popleft() # 큐의 값 왼쪽부터 빼기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if dist[nx][ny] == -1: # 방문 X
                # 벽 X
                if miro[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y]
                    queue.appendleft([nx, ny]) # 벽이 없는 곳 먼저 가야 하므로 큐의 제일 앞
                # 벽 O
                else:
                    dist[nx][ny] = dist[x][y] + 1 # 벽을 깨서 +1
                    queue.append([nx, ny]) # 벽이 있는 곳은 피해야 하므로 큐의 제일 뒤


n, m = map(int, input().split())
miro = []

for _ in range(m):
    miro.append(list(map(int, input())))

dist = [[-1] * n for _ in range(m)] # 벽 파괴 횟수

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

bfs(0, 0)
print(dist[m - 1][n - 1])
