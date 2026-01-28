import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            houses.append((i, j))
        elif graph[i][j] == 2:
            chickens.append((i, j))

answer = 1e9
chicken_list = []

def backtrack(depth, idx):
    global answer

    if depth == m:
        total = 0
        for h in houses:
            temp = 1e9
            for c in chicken_list:
                length = abs(h[0] - c[0]) + abs(h[1] - c[1])
                temp = min(temp, length)
            total += temp
        answer = min(answer, total)
        return

    for i in range(idx, len(chickens)): # 아직 방문 안 했다면?
        chicken_list.append(chickens[i])
        backtrack(depth + 1, i + 1)
        chicken_list.pop()

backtrack(0, 0)
print(answer)