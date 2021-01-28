import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))

heapq.heapify(cards)

for _ in range(M):
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, tmp)
    heapq.heappush(cards, tmp)



print(sum(cards))