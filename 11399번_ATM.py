# 입력 받기 위한 sys import
import sys

# 인원수 입력 받기
count = int(sys.stdin.readline())

# 인원별 걸리는 시간 입력 받기
time = list(map(int, sys.stdin.readline().split()))

# 오름차순 정렬
time.sort()

# 기다린 시간 초기화
wait_time = 0
# 걸리는 시간 초기화
sum_time = 0

# 인원별 걸리는 시간 계산
for i in time:
    wait_time += int(i)
    sum_time += wait_time

# 결과 출력
print(sum_time)