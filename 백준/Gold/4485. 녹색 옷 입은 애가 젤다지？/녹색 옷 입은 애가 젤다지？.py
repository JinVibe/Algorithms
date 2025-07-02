from collections import deque
import sys

n = int(input())

pn = 0  # problem number
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs():
    queue = deque()
    queue.append([0, 0])
    cost[0][0] = arr[0][0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if cost[y][x] + arr[ny][nx] < cost[ny][nx]:
                    cost[ny][nx] = cost[y][x] + arr[ny][nx]
                    queue.append([nx, ny])

    return cost[n - 1][n - 1]


while n != 0:
    pn += 1
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))

    cost = [[sys.maxsize for j in range(n)] for i in range(n)]

    print(f"Problem {pn}:", bfs())

    n = int(input())
