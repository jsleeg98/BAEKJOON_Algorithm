import sys

# - 구분자로 입력 나누기
arr = sys.stdin.readline().split('-')

# 결과 0으로 초기화
result = 0

# 0번째 내부 합 결과에 더하기
for i in arr[0].split('+'):
    result += int(i)

# 1번째 이후 내부 합 결과에 빼기
for i in arr[1:]:
    for j in i.split('+'):
        result -= int(j)

# 결과 출력
print(result)