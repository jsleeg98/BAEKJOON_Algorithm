import sys 

# 인원수 입력 받기
N = int(sys.stdin.readline())

# 앞에 키큰 사람 수 배열 입력 받기
array = list(map(int, sys.stdin.readline().split()))

# 정답
line = [] 
for i in range(N):
    line.append(0)

# 현재 줄 세운 사람 수
count = 0

# 뒤로 옯기는 함수
def move_back(count, i):
    for k in range(count - i):
        line[count - k] = line[count - 1 - k]

# 키 큰 사람부터 판단
for i in range(N - 1, -1, -1):
    move_back(count, array[i])
    line[array[i]] = N
    N -= 1
    count += 1


for i in line:
    print(i, end = ' ')