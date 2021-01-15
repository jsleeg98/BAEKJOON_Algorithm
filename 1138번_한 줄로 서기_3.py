import sys 

# 인원수 입력 받기
N = int(sys.stdin.readline())

# 앞에 키큰 사람 수 배열 입력 받기
array = list(map(int, sys.stdin.readline().split()))
array.reverse()
# 정답
line = [] 


# 키 큰 사람부터 판단
for i in range(N):
    line.insert(array[i], N)
    N -= 1



for i in line:
    print(i, end = ' ')