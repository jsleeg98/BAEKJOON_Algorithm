import sys

# 행렬의 크기
r, c = map(int, sys.stdin.readline().split())

# 행렬 초기화
problem = []
answer = []

# 행렬 입력 받기
for i in range(r):
    problem.append(list(map(int, sys.stdin.readline().rstrip())))

for i in range(r):
    answer.append(list(map(int, sys.stdin.readline().rstrip())))

# 행렬 연산 함수 3*3 뒤집기
def func(x, y):
    for i in range(x[0], x[0] + 3):
        for j in range(x[1], x[1] + 3):
            y[i][j] = 1 - y[i][j]
              

# 연산 횟수
count = 0
if r < 3 or c < 3:
    for i in range(r):
        for j in range(c):
            if(problem[i][j] != answer[i][j]):
                count = -1
else:
    for i in range(r-2):
        for j in range(c-2):
            if(problem[i][j] != answer[i][j]):
                func([i, j], problem)
                count += 1

# 행렬이 같아졌는지 확인   
if r < 3 or c < 3:
    if problem != answer:
        count = -1

# count 출력
print(count)
        