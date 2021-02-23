import sys

N = int(sys.stdin.readline())

# 각 줄의 숫자
numbers = []

for _ in range(N):
    numbers.append(list(map(int, sys.stdin.readline().split())))


for i in range(N - 1):
    for j in range(len(numbers[i + 1])):
        if j == 0:
            numbers[i + 1][j] = numbers[i][j] + numbers[i + 1][j]
        elif j == len(numbers[i + 1]) - 1:
            numbers[i + 1][-1] = numbers[i][-1] + numbers[i + 1][-1]
        else:
            numbers[i + 1][j] = max(numbers[i][j - 1] + numbers[i + 1][j], numbers[i][j] + numbers[i + 1][j])
    

print(max(numbers[-1]))
