import sys

input = sys.stdin.readline

R, C, M = map(int, input().split())

sharks = {}  # 시간 초과로 상어 있는 지역만 따로 저장

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[(r - 1, c - 1)] = [s, d, z]

UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4
sum = 0

for fisher in range(C):
    for r in range(R):
        if (r, fisher) in sharks:
            sum += sharks[(r, fisher)][2]  # 크기 획득
            del sharks[(r, fisher)]
            break

    # 고민 많이 함..
    new_sharks = {}

    for (r, c), (s, d, z) in sharks.items():
        # 머리로 계산함; (왕복 주기만큼 나눈 나머지만 이동)
        if d == UP or d == DOWN:
            if R > 1:
                cycle = (R - 1) * 2
                dist = s % cycle

                if d == UP:
                    r -= dist
                else:
                    r += dist

                while r < 0 or r >= R:
                    if r < 0:
                        r = -r
                        d = DOWN
                    elif r >= R:
                        r = (R - 1) * 2 - r
                        d = UP

        elif d == RIGHT or d == LEFT:
            if C > 1:
                cycle = (C - 1) * 2
                dist = s % cycle

                if d == LEFT:
                    c -= dist
                else:
                    c += dist

                while c < 0 or c >= C:
                    if c < 0:
                        c = -c
                        d = RIGHT
                    elif c >= C:
                        c = (C - 1) * 2 - c
                        d = LEFT

    # 상어가 이미 존재할 경우
        if (r, c) in new_sharks:
            if new_sharks[(r, c)][2] < z:
                new_sharks[(r, c)] = [s, d, z]
        else:
            new_sharks[(r, c)] = [s, d, z]

    sharks = new_sharks

print(sum)
