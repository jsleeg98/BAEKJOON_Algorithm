import sys

N = int(sys.stdin.readline())

weights = list(map(int, sys.stdin.readline().split()))

# 오름차순 정렬
weights.sort()

# 합
acc_sum = 0

for i in range(N):
    if acc_sum + 1 >= weights[i]:
        acc_sum += weights[i]
    else:
        break

print(acc_sum + 1)