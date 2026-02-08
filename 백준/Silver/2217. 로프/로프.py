# Greedy : 큰 것부터 쳐내기..
import sys

input = sys.stdin.readline

N = int(input())
weights = []

for _ in range(N):
    weights.append(int(input()))

weights.sort()

max_weight = 0

for i in range(N):
    summ = weights[i] * (N - i)
    max_weight = max(max_weight, summ)

print(max_weight)
