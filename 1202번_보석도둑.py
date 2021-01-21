import sys
import heapq

# 보석 N개, 가방 K개
N, K = map(int, sys.stdin.readline().split())

# 보석 무게, 가치 heap
gem = []

for _ in range(N):
    weight, value = map(int, sys.stdin.readline().split())
    heapq.heappush(gem, [weight, value])

# 가방 크기 heap
bag = []

for _ in range(K):
    heapq.heappush(bag, int(sys.stdin.readline()))

# 판단공간 초기화
judge = []
# 결과 0으로 초기화
result = 0

for i in range(K):
    # 가용무게는 가방에서 오름차순 순서대로 설정
    capacity = heapq.heappop(bag)
    # 보석이 남아있고 보석의 무게가 가용무게보다 작을동안
    while len(gem) > 0 and capacity >= gem[0][0]:
        weight = heapq.heappop(gem)[1]
        # -로 heap에 넣어야 가치가 가장 큰 보석이 맨 앞에 온다.
        heapq.heappush(judge, -weight)
    
    # 판단 공간에 보석이 있다면
    if len(judge) > 0:
        # 결과는 -로 가치가 되어있기 때문에 -로 다시 취해준다.
        result -= heapq.heappop(judge)



# 결과 출력
print(result)