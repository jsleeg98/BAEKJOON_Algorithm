import sys

N = int(sys.stdin.readline())

# 각 줄의 숫자
numbers = []

for _ in range(N):
    numbers.append(list(map(int, sys.stdin.readline().split())))


for i in range(N - 1):
    for j in range(len(numbers[i + 1])):
        # 맨 앞은 맨 앞끼리 합
        if j == 0:
            numbers[i + 1][j] = numbers[i][j] + numbers[i + 1][j]
        # 맨 뒤는 맨 뒤끼리 합
        elif j == len(numbers[i + 1]) - 1:
            numbers[i + 1][-1] = numbers[i][-1] + numbers[i + 1][-1]
        # 중간은 최대 값으로 저장
        else:
            numbers[i + 1][j] = max(numbers[i][j - 1] + numbers[i + 1][j], numbers[i][j] + numbers[i + 1][j])
    

print(max(numbers[-1]))
