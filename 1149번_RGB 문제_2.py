import sys

# 집의 개수 입력
N = int(sys.stdin.readline())

RGB_cost = []

for _ in range(N):
    RGB_cost.append(list(map(int, sys.stdin.readline().split())))


# 비용 초기화
cost = []

# 비용 리스트 초기화
for _ in range(N):
    cost.append([0, 0, 0])

# 집의 개수 만큼 반복
for i in range(N):
    # 첫번째 집의 경우 초기화 과정
    if i == 0:
        cost[i][0] = RGB_cost[i][0]
        cost[i][1] = RGB_cost[i][1]
        cost[i][2] = RGB_cost[i][2]
    # 두번째 집 부터 점화식 사용
    # 각각 색상을 선택할 때 이전 과정에서 가장 최소 비용인 경우를 현재 색상의 비용으로 저장
    else:
        cost[i][0] = RGB_cost[i][0] + min(cost[i - 1][1], cost[i - 1][2])
        cost[i][1] = RGB_cost[i][1] + min(cost[i - 1][0], cost[i - 1][2])
        cost[i][2] = RGB_cost[i][2] + min(cost[i - 1][0], cost[i - 1][1])
    
# 비용 중 가장 작은 값 출력
print(min(cost[N-1]))
