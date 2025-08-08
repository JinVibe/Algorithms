import sys
input = sys.stdin.readline

N = int(input())
solution = sorted(list(map(int, input().split())))

start = 0
end = N-1

target = abs(solution[0] + solution[-1])
result = [solution[0], solution[-1]]

while start < end:
    l = solution[start]
    r = solution[end]

    d = l + r
    zero_d = abs(d)

    if zero_d < target:
        target = zero_d
        result = [l, r]

    if d < 0:
        start += 1
    else:
        end -= 1

print(*result)