import sys

N = int(sys.stdin.readline())

RGB_cost = []

for _ in range(N):
    RGB_cost.append(list(map(int, sys.stdin.readline().split())))


# 비용 초기화
cost = [0, 0, 0]

# 처음 집을 R, G, B로 칠할 때 각각의 경우에 나오는 비용 계산
for j in range(3):
    cost[j] += RGB_cost[0][j]
    # 첫번째 집 칠한 색 인덱스 저장
    RGB = j
    for i in range(1, N):
        tmp = RGB_cost[i]
        del tmp[RGB]
        RGB = RGB_cost[i].index(min(tmp))
        cost[j] += min(tmp)
    
# 비용 중 가장 작은 값 출력
print(min(cost))