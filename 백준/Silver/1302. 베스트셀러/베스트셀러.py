import sys

input = sys.stdin.readline

N = int(input())
books = {}

for _ in range(N):
    book = input().strip()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

books = dict(sorted(books.items()))

for b in books:
    if books[b] == max(books.values()):
        print(b)
        break