# 자신보다 크기가 크다면 지나갈 수 X
# 자신과 크기가 같다면 지나갈 수 O, 먹을 수 X
# 자신보다 크기가 작다면 먹을 수 O

# 먹을 수 있는 물고기가 없을 때 도움 요청
# 먹을 수 있는 물고기가 1마리일 때 먹으러 감
# 먹을 수 있는 물고기가 2마리 이상일 때 거리가 가장 가까운 물고기를 먹으러 감
# 거리가 같은 먹을 수 있는 물고기가 여러 마리일 때 우선순위 1. 가장 위, 2. 가장 왼쪽

# 사고의 흐름
# 1. 제일 가까운 거 먼저 먹으니 BFS로 처리하자
# 2.
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

INF = 1e9
shark_size = 2

# 현재 위치 뽑아내기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            now_x, now_y = i, j
            graph[i][j] = 0

# 시작 위치 넣고
def BFS():
    queue = deque([(now_x, now_y)])

    visited = [[-1] * n for _ in range(n)]
    visited[now_x][now_y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if shark_size >= graph[nx][ny] and visited[nx][ny] == -1:  # 문제에 따른 shark_size 조건 추가
                    visited[nx][ny] = visited[x][y] + 1 # 내 걸음 수 기록
                    queue.append((nx, ny))

    return visited


def solve(visited):
    x, y = 0, 0
    min_distance = INF
    # 최소값인 위치와 그 값
    for i in range(n):
        for j in range(n):
            if visited[i][j] != -1 and 1 <= graph[i][j] < shark_size:
                if visited[i][j] < min_distance:
                    min_distance = visited[i][j]
                    x, y = i, j

    if min_distance == INF:
        return False
    else:
        return x, y, min_distance

answer = 0
food = 0

while True: # BFS 반복
    result = solve(BFS())

    if not result:
        print(answer)
        break
    else:
        now_x, now_y = result[0], result[1]
        answer += result[2]
        graph[now_x][now_y] = 0
        food += 1

    if food >= shark_size:
        shark_size += 1
        food = 0
