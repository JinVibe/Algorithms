import sys

input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())  # 처음 위치와 방향

# 내가 이 아이디어를 떠올릴 수 있었던 문제의 포인트는?
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

cnt = 0


def check(x, y):
    return 0 <= x < n and 0 <= y < m


while True:
    if room[r][c] == 0:
        room[r][c] = 100
        cnt += 1

    for _ in range(4):
        d = (d - 1) % 4
        nx, ny = r + dx[d], c + dy[d]
        if room[nx][ny] == 0 and check(nx, ny):
            r, c = nx, ny
            break

    else:
        r, c = r + dx[d] * (-1), c + dy[d] * (-1)
        if room[r][c] == 1 and check(r, c) or not check(r, c):
            print(cnt)
            exit(0)
