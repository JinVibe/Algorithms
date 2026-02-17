# 격자의 행과 열은 1번부터 N번까지 번호가 매겨져 있고, 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다.
# % 연산 쓰기

import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

fireballs = {}

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(M):  # M개의 파이어볼
    r, c, m, s, d = map(int, input().split())
    fireballs[(r - 1, c - 1)] = [(m, s, d)]

for _ in range(K):
    new_fireballs = {}
    # 1. 이동
    for (r, c), balls in fireballs.items():
        for m, s, d in balls:  # balls[0], balls[1], balls[2] 쓰기 싫어서 반복 1번인데 사용!
            nr = (r + dx[d] * s) % N
            nc = (c + dy[d] * s) % N

            if (nr, nc) not in new_fireballs:
                new_fireballs[(nr, nc)] = []  # 리스트화 시키기 위함
            new_fireballs[(nr, nc)].append((m, s, d))

    fireballs = {}

    for (r, c), balls in new_fireballs.items():
        if len(balls) == 1:
            fireballs[(r, c)] = [balls[0]]
        else:
            # 2개 이상이면 합치고 4분할
            sum_m, sum_s, count_odd, count_even = 0, 0, 0, 0
            total_count = len(balls)

            for m, s, d in balls:
                sum_m += m
                sum_s += s
                if d % 2 == 0:
                    count_even += 1
                else:
                    count_odd += 1

            nm = sum_m // 5  # 질량 계산
            if nm == 0:
                continue  # 질량 0이면 소멸 (저장 안 함)

            ns = sum_s // total_count  # 속력 계산

            # 방향 정하기 (핵심!)
            # 모두 홀수(홀수 개수 == 전체 개수) 이거나, 모두 짝수(짝수 개수 == 전체 개수)
            if count_odd == total_count or count_even == total_count:
                nd_list = [0, 2, 4, 6]
            else:
                nd_list = [1, 3, 5, 7]

            # 4개로 쪼개서 저장
            if (r, c) not in fireballs:
                fireballs[(r, c)] = []
            for nd in nd_list:
                fireballs[(r, c)].append((nm, ns, nd))

ans = 0

for balls in fireballs.values():
    for m, s, d in balls:
        ans += m

print(ans)