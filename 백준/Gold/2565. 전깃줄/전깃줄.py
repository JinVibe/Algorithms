import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
lines = sorted(tuple(map(int, input().split())) for _ in range(N))  # A 기준 정렬

increase = [] # 최장 증가 부분 수열(LIS, Longest Increasing Subsequence)
              # 가장 길게 증가하는 수열의 길이 찾기

for _, num in lines:  # 8,2,9,1,4,6,7,10
    idx = bisect_left(increase, num)  # 0,0,1,0,1,2,3,4,3

    if idx == len(increase):
        increase.append(num)
    else:
        increase[idx] = num # 8을 2가 새로 들어와서 덮어씀

print(N - len(increase))

# [8]
# [2]
# [2, 9]
# [1, 9]
# [1, 4]
# [1, 4, 6]
# [1, 4, 6, 7]
# [1, 4, 6, 7, 10]