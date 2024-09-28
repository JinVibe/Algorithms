def dfs(v):
    visited[v] = 1
    nex = arr[v]

    if visited[nex] == 0:
        dfs(nex)
    return


t = int(input())

for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)  # 기본 : 방문 여부
    cnt = 0

    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i)
            cnt += 1
    print(cnt)
