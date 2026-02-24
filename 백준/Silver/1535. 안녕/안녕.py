import sys

input = sys.stdin.readline

N = int(input())

health = list(map(int, input().split()))
joy = list(map(int, input().split()))

dp = [0] * 100

ans = 0

for h, j in zip(health, joy):
    for i in range(99, h - 1, -1):
        dp[i] = max(dp[i], dp[i - h] + j)

ans = max(dp)
print(ans)
