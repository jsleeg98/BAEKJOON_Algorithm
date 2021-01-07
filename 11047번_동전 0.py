import sys

N, K = map(int, sys.stdin.readline().split())

# 동전 리스트
coins = []

# 동전 리스트 입력
for i in range(N):
    temp = int(sys.stdin.readline())
    coins.append(temp)

# 동전 개수 초기화
count = 0

for i in range(-1, -N-1, -1):
    if K >= coins[i]:
        count += K // coins[i]
        K = K % coins[i]
    if K == 0:
        break

print(count)

