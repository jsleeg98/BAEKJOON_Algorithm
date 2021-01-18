import sys
import heapq

# 카드 묶음 수
N = int(sys.stdin.readline())

# 카드 개수 리스트
cards = []

for _ in range(N):
    heapq.heappush(cards, int(sys.stdin.readline().rstrip()))

# 오름차순 정렬
# cards.sort()

# 리스트를 큐에 담기
# cards_que = deque(cards)

# 결과 초기화
result = 0

# 큐로 구현
# 큐 앞에서부터 꺼내서 비교 횟수 계산
# 계산한 횟수를 오름차순에 맞게 큐에 다시 집어넣기
# 큐에 아무것도 남기 않을 때 까지 반복
# while(len(cards_que) > 1):
#     tmp = cards_que.popleft() + cards_que.popleft()
#     result += tmp
#     index = 0
#     for i in range(0, len(cards_que)):
#         if len(cards_que) == 1:
#             break
#         elif tmp > cards_que[i]:
#             index += 1
#         else:
#             break
#     cards_que.insert(index, tmp)


# 리스트로 구현
# while len(cards) > 1:
#     tmp_1 = min(cards)
#     cards.remove(tmp_1)
#     tmp_2 = min(cards)
#     cards.remove(tmp_2)
#     result += tmp_1 + tmp_2
#     cards.append(tmp_1 + tmp_2)

# heap으로 구현
while len(cards) > 1:
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    result += tmp
    heapq.heappush(cards, tmp)


print(result)