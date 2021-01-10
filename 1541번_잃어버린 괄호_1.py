import sys

# 식을 - 구분자로 입력받기
minus = sys.stdin.readline().split('-')


for i in range(len(minus)):
    # + 구분자로 나누기
    plus = minus[i].split('+')
    # 내부 합 0으로 초기화
    plus_result = 0
    # + 연산을 먼저 수행
    for j in range(len(plus)):
        plus_result += int(plus[j])
        minus[i] = plus_result

# - 연산 전 결과 초기화
minus_result = minus[0]

# - 연산 수행
for i in range(1, len(minus)):
    minus_result -= int(minus[i])

print(minus_result)