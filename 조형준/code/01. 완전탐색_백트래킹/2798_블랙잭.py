from sys import stdin

from itertools import combinations

n, m = map(int, stdin.readline().split())
cards = list(map(int, stdin.readline().split()))

sub_ = int(1e9)
res = 0

for cards_p in list(combinations(cards, 3)):
    p = sum(cards_p)

    if p > m:
        continue

    if p == m:
        res = p
        break

    k = m - p

    if k < sub_:
        sub_ = k
        res = p

print(res)
