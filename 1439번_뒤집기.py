import sys

# 입력 받기
array = list(map(int, sys.stdin.readline().rstrip()))

# 맨 처음 기준 설정
criterion = array[0]

# 바뀐 횟수 0으로 초기화
count = 0

# 바뀐 횟수 세기
for i in range(1, len(array)):
    if criterion != array[i]:
        criterion = array[i]
        count += 1

# 바뀐 횟수가 짝수면 2로 나눈 몫이 결과
if count % 2 == 0:
    result = count // 2
# 바뀐 횟수가 홀수면 2로 나눈 몫에 1을 더한 값이 결과
else:
    result = (count // 2) + 1

# 결과 출력
print(result)
