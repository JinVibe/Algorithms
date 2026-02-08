import sys

input = sys.stdin.readline

H, W = map(int, input().split())

city = []
for _ in range(H):
    city.append(list(input().strip()))

time = [ [-1] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if city[i][j] == 'c':
            time[i][j] = 0
        elif city[i][j] == '.':
            if 'c' not in city[i][:j]:
                time[i][j] = -1
            else:
                time[i][j] = time[i][j-1] + 1

for i in range(H):
    print(*time[i])
