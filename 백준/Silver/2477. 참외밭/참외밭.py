import sys

input = sys.stdin.readline

K = int(input())

dirs = []
lengths = []

for _ in range(6):
    dir, length = map(int, input().split())

    dirs.append(dir)
    lengths.append(length)

if dirs.count(1) == 2:  # 서쪽이 제일 김
    idx_width = dirs.index(2)
    width = lengths[idx_width]
else:
    idx_width = dirs.index(1)
    width = lengths[idx_width]

if dirs.count(3) == 2:  # 북쪽이 제일 김
    idx_height = dirs.index(4)
    height = lengths[idx_height]
else:
    idx_height = dirs.index(3)
    height = lengths[idx_height]

if idx_width < idx_height:
    print((width * height - lengths[idx_width - 3] * lengths[(idx_height + 3) % 6]) * K)
else:
    print((width * height - lengths[idx_height - 3] * lengths[(idx_width + 3) % 6]) * K)