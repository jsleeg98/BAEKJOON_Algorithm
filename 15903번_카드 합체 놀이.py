import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))

# 힙으로 저장
heapq.heapify(cards)

# 카드 합치기 횟수만큼 반복
for _ in range(M):
    # 가장 작은 값 두개 꺼내서 합 구하기
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    # 구한 합 다시 집어 넣기
    heapq.heappush(cards, tmp)
    heapq.heappush(cards, tmp)

# 총합 출력
print(sum(cards))