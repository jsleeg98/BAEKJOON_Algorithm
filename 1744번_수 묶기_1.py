import sys

# 숫자 개수
N = int(sys.stdin.readline())

# 숫자 배열 입력
minus = []
plus = []
one = []

# 결과 0으로 초기화
maximum = 0

for _ in range(N):
    tmp = int(sys.stdin.readline())
    if tmp > 0 :
        if tmp == 1:
            one.append(tmp)
        else:
            plus.append(tmp)
    else:
        minus.append(tmp)


# minus는 오름차순 정렬
minus.sort()
# plus는 내림차순 정렬
plus.sort(reverse= True)

def multi_plus(x):
    result = 0
    # 리스트 길이가 짝수인 경우
    if len(x) % 2 == 0:
        for i in range(0, len(x), 2):
            result += x[i] * x[i + 1]
    # 리스트 길이가 홀수인 경우
    else:
        for i in range(0, len(x) - 1, 2):
            result += x[i] * x[i + 1]
        # 남은 원소 더해주기
        result += x[len(x) - 1]
    return result

# 결과 연산
maximum = multi_plus(minus) + multi_plus(plus) + len(one)

print(maximum)