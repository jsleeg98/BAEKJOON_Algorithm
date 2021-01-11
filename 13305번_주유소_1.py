import sys

# 도시의 수
N = int(sys.stdin.readline())

# 도로 길이
roads = list(map(int, sys.stdin.readline().split()))

# 도시당 기름 비용
costs = list(map(int, sys.stdin.readline().split()))


# 총 비용
result = 0

# 최소 기름 값 초기화
m = costs[0]

for i in range(N - 1):
    if m > costs[i]:
        m = costs[i]
    result += m * roads[i]
 
print(result)
